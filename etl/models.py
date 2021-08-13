"""
Python class for output db model definition
author: Damien Michelle
date: 13/08/2021
"""
import sqlite3


class DB:

    def __init__(self, db_file):
        self.connexion = sqlite3.connect(db_file)
        self.cursor = self.connexion.cursor()
        self._init_db()

    def _init_db(self):
        output_table = """
        CREATE TABLE IF NOT EXISTS premium_payments_transformed(
        MEMBER_ID INTEGER
        TYPE INTEGER
        DATE_START TEXT
        DATE_END TEXT
        )
        """

        self.cursor.execute(output_table)
