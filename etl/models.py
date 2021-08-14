"""
Python class for output db model definition
author: Damien Michelle
date: 13/08/2021
"""
import sqlite3


class DB:
    """
    Class for sqlite database output
    """

    def __init__(self, db_file):
        """
        Init connexion and cursor
        :param db_file: name of sqlite database
        """
        self.connexion = sqlite3.connect(db_file)
        self.cursor = self.connexion.cursor()
        self._init_db()

    def _init_db(self):
        """
        Initialize output database
        :return: a table in sqlite database
        """
        output_table = """
        CREATE TABLE IF NOT EXISTS premium_payments_transformed(
        MEMBER_ID INTEGER
        TYPE INTEGER
        DATE_START TEXT
        DATE_END TEXT
        )
        """

        self.cursor.execute(output_table)
