"""
Main file where the etl_premium_clients is performed
author: Damien Michelle
date: 13/08/2021
"""
import os
import sys

from etl_premium_clients.utils import parse_args
from etl_premium_clients.base_logger import logging
from etl_premium_clients.config import CURRENT_DIR, DB_DIR
from etl_premium_clients.PerformETL import PerformETL


def main(input_db, input_table, custom_path, output_name_db):
    """
    Main function where ETL pipeline is executed
    :return:
    """
    try:
        path_db = input_db if custom_path else os.path.join(CURRENT_DIR, DB_DIR, input_db)
        db_name = input_table
        output_name_db = output_name_db

        perform_transformation = PerformETL(path_db, db_name, output_name_db)
        perform_transformation.perform_etl()
        logging.info('SUCCESS - All scripts have been executed with success ! '
                     'Congratulations!')
    except Exception as err:
        logging.info(f'ERROR - during the execution of the script: {err}')


if __name__ == "__main__":
    ARGS = parse_args(args=sys.argv[1:])
    INPUT_DB = ARGS.input_db
    INPUT_TABLE = ARGS.input_table
    CUSTOM_PATH = ARGS.custom_path
    OUTPUT_NAME_DB = ARGS.output_name_db
    main(INPUT_DB, INPUT_TABLE, CUSTOM_PATH, OUTPUT_NAME_DB)
