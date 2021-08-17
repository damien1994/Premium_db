"""
Python class for extract transform load actions
author: Damien Michelle
date: 13/08/2021
"""
import os
import sqlite3
import numpy as np
import pandas as pd

from etl.base_logger import logging
from etl.config import DATES_COLS, CURRENT_DIR
from etl.models import DB


class PerformETL:
    """
    Class for ETL pipeline
    """

    def __init__(self, path_db, table_name):
        self.path_db = path_db
        self.table_name = table_name

    def perform_etl(self):
        """
        Full ETL process
        Steps are:
        - Extract data from sqlite database
        - Transform data by grouping consecutive payments from the same client
        - Load data to new sqlite database db_transformed.db
        """
        try:
            dataframe = self.extract()
            logging.info('SUCCESS - Data extraction has been performed')
            df_transformed = self.transform(dataframe)
            logging.info('SUCCESS - Data transformation has been performed')
            del dataframe
            self.load(df_transformed)
            logging.info('SUCCESS - Data load has been performed')
        except ValueError as err:
            logging.info(f'ERROR - ETL pipeline has failed : {err}')

    def extract(self) -> pd.DataFrame:
        """
        Extract data from sqlite database
        :return: a pandas dataframe
        """
        try:
            full_path = os.path.join(self.path_db)
            query = f'SELECT * FROM {self.table_name}'
            connexion = sqlite3.connect(full_path)
            return pd.read_sql_query(query, connexion, parse_dates=DATES_COLS)
        except (ValueError, AssertionError) as err:
            logging.info(f'ERROR - during the extract step : {err}')

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply transformations to pandas dataframe output
        :param df: a pandas DataFrame
        :return: a pandas DataFrame transformed
        """
        try:
            df['transaction_class'] = \
                self._group_transaction(df, ['member_id', 'type'],
                                        'date_end', 'date_start', 3)
            logging.info('SUCCESS - during transformation step - '
                         'transaction grouping has succeeded')
            #TO DO : add percentage of same / other transaction in logging
            result = df.groupby(['member_id', 'type', 'transaction_class']).agg({
                'date_start': min,
                'date_end': max
            }
            )
            return result.reset_index().drop('transaction_class', axis=1)
        except ValueError as err:
            logging.info(f'ERROR - during the transform step : {err}')

    @staticmethod
    def load(data: pd.DataFrame):
        """
        Get pandas dataframe transformed and store result into sqlite db
        :param data: a pandas dataframe
        :return: a sqlite database
        """
        try:
            full_path = os.path.join(CURRENT_DIR, 'db/output/db_test_container.sqlite3')
            output_db = DB(full_path)
            data.to_sql('premium_payments_transformed', output_db.connexion,
                        if_exists='replace', index=False)
        except ValueError as err:
            logging.info(f'ERROR - Data load has failed: {err}')

    @staticmethod
    def _group_transaction(df: pd.DataFrame,
                           group_cols: list,
                           end_date_col: str,
                           start_date_col: str,
                           freq: int) -> np.ndarray:
        """
        Python function to define if, for a client and a subscription type,
        the client is paying for the same subscription or not
        :param df: a pandas dataframe
        :param group_cols: list of cols to groupby
        :param end_date_col: end date of monthly subscription
        :param start_date_col: start date of monthly subscription
        :param freq: business rule for defining if it's the same subscription or not
        :return: a pandas series
        """
        try:
            df_sorted = df.sort_values(by=group_cols+[start_date_col])
            del df
            df_sorted[f'{end_date_col}_lag'] = df_sorted.groupby(group_cols)[end_date_col].shift(1)
            return np.where(
                df_sorted[f'{end_date_col}_lag'] + pd.Timedelta(freq, unit='D') < df_sorted[start_date_col],
                'other_transaction',
                'same_transaction'
            )
        except ValueError as err:
            logging.info(f'ERROR - during transform step '
                         f'- grouping transaction substep : {err}')
