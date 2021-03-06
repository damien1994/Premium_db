"""
Test file pour performing etl_premium_clients
author: Damien Michelle
date: 13/08/2021
"""
import pytest
import pandas as pd

from etl_premium_clients.PerformETL import PerformETL
# TO DO : test extract and load steps


@pytest.fixture
def input_data():
    data = {
        'member_id': [1, 1, 1, 1, 2],
        'date_start': ['2018-10-31', '2018-12-01', '2019-01-10', '2019-02-10', '2020-01-01'],
        'date_end': ['2018-11-30', '2019-01-01', '2019-02-09', '2019-03-11', '2020-02-01'],
        'type': [1, 1, 1, 2, 3]
    }
    input_df = pd.DataFrame(data)
    input_df['date_start'] = pd.to_datetime(input_df['date_start'])
    input_df['date_end'] = pd.to_datetime(input_df['date_end'])
    return input_df


@pytest.fixture
def output_data():
    data = {
        'member_id': [1, 1, 1, 2],
        'type': [1, 1, 2, 3],
        'date_start': ['2019-01-10', '2018-10-31', '2019-02-10', '2020-01-01'],
        'date_end': ['2019-02-09', '2019-01-01', '2019-03-11', '2020-02-01'],
    }
    df_expected = pd.DataFrame(data)
    df_expected['date_start'] = pd.to_datetime(df_expected['date_start'])
    df_expected['date_end'] = pd.to_datetime(df_expected['date_end'])
    return df_expected


def test_transform(input_data, output_data):
    """
    Test transformation process of ETL
    """
    fake_path_db = 'fake_db.db'
    fake_table_name = 'fake_table_name'
    fake_output_db_name = 'fake_output_db_name'
    etl = PerformETL(fake_path_db, fake_table_name, fake_output_db_name)
    df_result = etl.transform(input_data)
    print(df_result)
    print(output_data)
    assert df_result.equals(output_data)
