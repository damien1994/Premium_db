class DB:

    def __init__(self, db_file):
        self.db_file = db_file

    def _init_db(self):
        output_table = """
        CREATE TABLE IF NOT EXISTS output_db(
        MEMBER_ID INTEGER
        TYPE INTEGER
        DATE_START DATE
        DATE_END
        """