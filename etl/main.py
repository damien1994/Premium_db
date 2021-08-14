"""
Main file where the etl is performed
author: Damien Michelle
date: 13/08/2021
"""
import os

from etl.base_logger import logging
from etl.config import CURRENT_DIR, DB_DIR
from etl.PerformETL import PerformETL


def main():
    """
    Main function where ETL pipeline is executed
    :return:
    """
    try:
        path_db = os.path.join(CURRENT_DIR, DB_DIR, 'db.db')
        db_name = 'premium_payments'

        perform_transformation = PerformETL(path_db, db_name)
        perform_transformation.perform_etl()
        logging.info('SUCCESS - All scripts have been executed with success ! '
                     'Congratulations!')
    except Exception as err:
        logging.info(f'ERROR - during the execution of the script: {err}')


if __name__ == "__main__":
    main()
