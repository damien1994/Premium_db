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

    def extract(self):
        full_path = os.path.join(self.path_db)
        query = f'SELECT * FROM {self.table_name}'
        connexion = sqlite3.connect(full_path)
        return pd.read_sql_query(query, connexion, parse_dates=DATES_COLS)

    def transform(self, df: pd.DataFrame):
        df['transaction_class'] = self._group_transaction(df, ['member_id', 'type'], 'date_end', 'date_start', 3)
        result = df.groupby(['member_id', 'type', 'transaction_class']).agg({
            'date_start': min,
            'date_end': max
        }
        )
        return result.reset_index().drop('transaction_class', axis=1)

    @staticmethod
    def load(data: pd.DataFrame):
        try:
            full_path = os.path.join(CURRENT_DIR, 'db/db_transformed.sqlite3')
            output_db = DB(full_path)
            data.to_sql('premium_payments_transformed', output_db.connexion, if_exists='replace', index=False)
        except ValueError as err:
            logging.info(f'ERROR - Data load has failed: {err}')

    @staticmethod
    def _group_transaction(df, group_cols, end_date_col, start_date_col, freq):
        df[f'{end_date_col}_lag'] = df.groupby(group_cols)[end_date_col].shift(1)
        return np.where(
            df[start_date_col] + pd.Timedelta(freq, unit='D') < df[f'{end_date_col}_lag'],
            'other_transaction',
            'same_transaction'
        )
