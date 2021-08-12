import sqlite3
import numpy as np
import pandas as pd

from etl.config import DATES_COLS
from etl.models import DB


class PerformETL:

    def __init__(self, path_db, db_name):
        self.path_db = path_db
        self.db_name = db_name

    def extract(self):
        query = f'SELECT * FROM {self.db_name}'
        connexion = sqlite3.connect(self.path_db)
        return pd.read_sql_query(query, connexion, parse_dates=DATES_COLS)

    def transform(self, df):
        df['transaction_class'] = self._group_transaction(df, ['member_id', 'type'], 'date_end', 'date_start', 3)
        result = df.groupby(['member_id', 'type', 'transaction_class']).agg({
            'date_start': min,
            'date_end': max
        }
        )
        return result.reset_index().drop('transaction_class', axis=1)

    def load(self, data):
        output_db = DB()
        data.to_sql(f'{self.db_name}_transformed', output_db)

    @staticmethod
    def _group_transaction(df, group_cols, end_date_col, start_date_col, freq):
        df[f'{end_date_col}_lag'] = df.groupby(group_cols)[end_date_col].shift(1)
        return np.where(
            df[start_date_col] + pd.Timedelta(freq, unit='D') < df[f'{end_date_col}_lag'],
            'other_transaction',
            'same_transaction'
        )
