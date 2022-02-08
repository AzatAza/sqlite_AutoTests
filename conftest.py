import logging
import random
import sqlite3
from sqlite3 import Error
import pytest

logger = logging.getLogger("moodle")
logger_api = logging.getLogger("api")


def random_1_to(x):
    return random.randint(1, x)


def pytest_addoption(parser):
    parser.addoption(
        "--path",
        action="store",
        default=r"..\Wargaming\test\ships.db",
        help="Path to data base",
    )


@pytest.fixture
def session():
    connection = sqlite3.connect(r"E:\Test Tasks\Wargaming\test\ships.db")
    db_session = connection.cursor()
    yield db_session
    connection.close()


@pytest.fixture
def in_memory_session():
    connection = sqlite3.connect(r"file:foobar?mode=memory&cache=shared")
    db_session = connection.cursor()
    yield db_session
    connection.close()


@pytest.fixture
def randomazied_db():
    try:
        old_db = sqlite3.connect(r"E:\Test Tasks\Wargaming\test\ships.db")
        new_db = sqlite3.connect("file:foobar?mode=memory&cache=shared")
        old_db_cursor = old_db.cursor()
        new_db_cursor = new_db.cursor()

        print("База данных создана и успешно подключена к SQLite")
        with open(r'E:\Test Tasks\Wargaming\sql_query_create_tables.sql', 'r') as sqlite_file:
            sql_script = sqlite_file.read()
        new_db_cursor.executescript(sql_script)

        old_db_cursor.execute("ATTACH DATABASE 'file:foobar?mode=memory&cache=shared' as new")
        old_db_cursor.execute("INSERT INTO new.Ships SELECT * FROM Ships;")
        old_db_cursor.execute("INSERT INTO new.Weapons SELECT * FROM Weapons")
        old_db_cursor.execute("INSERT INTO new.Hulls SELECT * FROM Hulls")
        old_db_cursor.execute("INSERT INTO new.Engines SELECT * FROM Engines")
        old_db_cursor.connection.commit()
        new_db_cursor.connection.commit()
        new_db_cursor.execute("SELECT count() FROM Ships")
        rows_amount = new_db_cursor.fetchall()
        new_db_cursor.execute("SELECT count() FROM pragma_table_info('Ships')")
        columns_amount = new_db_cursor.fetchall()
        print(rows_amount[0][0])
        for i in range(rows_amount[0][0]):
            dice = random.randint(2, columns_amount[0][0])
            new_db_cursor.execute(f"SELECT name FROM pragma_table_info('Ships') WHERE ROWID = {dice}")
            column_name = new_db_cursor.fetchone()
            new_db_cursor.execute(f"SELECT count() FROM {column_name[0]}s")
            new_db_cursor.execute(f"UPDATE Ships SET {column_name[0]} = {column_name[0]}-{random_1_to(99999999)} "
                                  f"WHERE ROWID = {i}")

        for i in range(2, columns_amount[0][0] + 1):
            new_db_cursor.execute(f"SELECT name FROM pragma_table_info('Ships') WHERE ROWID = {i}")
            table_name = new_db_cursor.fetchone()
            new_db_cursor.execute(f"SELECT count() FROM {table_name[0]}s")
            rows_amount = new_db_cursor.fetchall()
            new_db_cursor.execute(f"SELECT count() FROM pragma_table_info('{table_name[0]}s')")
            columns_amount = new_db_cursor.fetchall()

            for j in range(rows_amount[0][0] + 1):
                dice = random.randint(2, columns_amount[0][0])
                new_db_cursor.execute(f"SELECT name FROM pragma_table_info('{table_name[0]}s') WHERE ROWID = {dice}")
                column_name = new_db_cursor.fetchone()
                new_db_cursor.execute(f"UPDATE {table_name[0]}s SET {column_name[0]} = '{random_1_to(9999999)}' "
                                      f"WHERE ROWID = {j}")
        old_db_cursor.connection.commit()
        new_db_cursor.connection.commit()
    except Error as error:
        print("Ошибка при подключении к sqlite", error)
