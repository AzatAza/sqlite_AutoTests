class GetDBData:
    def __init__(self, new_db_data=None, old_db_data=None, ):
        self.new_db_data = new_db_data
        self.old_db_data = old_db_data

    @staticmethod
    def new_db_data(row, col, in_memory_session) -> str:
        in_memory_session.execute(f"SELECT name FROM pragma_table_info('Ships') WHERE ROWID = 1")
        ship_name = in_memory_session.fetchone()[0]
        in_memory_session.execute(f"SELECT name FROM pragma_table_info('Ships') WHERE ROWID = {col}")
        column_name = in_memory_session.fetchone()[0]
        in_memory_session.execute(f"SELECT {ship_name}, {column_name} FROM Ships WHERE ROWID = {row}")
        new_db_data = in_memory_session.fetchone()
        return new_db_data

    @staticmethod
    def old_db_data(row, col, session):
        session.execute(f"SELECT name FROM pragma_table_info('Ships') WHERE ROWID = 1")
        ship_name = session.fetchone()[0]
        session.execute(f"SELECT name FROM pragma_table_info('Ships') WHERE ROWID = {col}")
        column_name = session.fetchone()[0]
        session.execute(f"SELECT {ship_name}, {column_name} FROM Ships WHERE ROWID = {row}")
        old_db_data = session.fetchone()
        return old_db_data
