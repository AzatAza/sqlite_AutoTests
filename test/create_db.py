import random
import sqlite3
from sqlite3 import Error


def create_db():
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect("ships.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")

        with open('../sql_query_create_tables.sql', 'r') as sqlite_file:
            sql_script = sqlite_file.read()
        cursor.executescript(sql_script)
        print("Скрипт SQLite успешно выполнен")

        num = list(range(1, 201))
        random.shuffle(num)

        for i in range(200):
            ship_name = f'Ship-{num[i]}'
            weapon_name = f'weapon-{random.randint(1, 20)}'
            hull_name = f'hull-{random.randint(1, 5)}'
            engine_name = f'engine-{random.randint(1, 6)}'
            cursor.execute("""INSERT INTO Ships(ship, weapon, hull, engine)
               VALUES(?, ?, ?, ?);""", (ship_name, weapon_name, hull_name, engine_name))

        num = list(range(1, 21))
        random.shuffle(num)
        for i in range(20):
            weapon_name = f'Weapon-{num[i]}'
            reload_speed = random.randint(1, 20)
            rotation_speed = random.randint(1, 20)
            diameter = random.randint(1, 20)
            power_volley = random.randint(1, 20)
            count = random.randint(1, 20)
            cursor.execute("""INSERT INTO Weapons(weapon, reload_speed, rotation_speed, diameter, power_volley, count)
               VALUES(?, ?, ?, ?, ?, ?);""", (weapon_name, reload_speed, rotation_speed, diameter, power_volley, count))

        num = list(range(1, 6))
        random.shuffle(num)
        for i in range(5):
            hull_name = f'Hull-{num[i]}'
            armor = random.randint(1, 20)
            type = random.randint(1, 20)
            capacity = random.randint(1, 20)
            cursor.execute("""INSERT INTO Hulls(hull, armor, type, capacity)
               VALUES(?, ?, ?, ?);""", (hull_name, armor, type, capacity))

        num = list(range(1, 7))
        random.shuffle(num)
        for i in range(6):
            engine_name = f'Engine-{num[i]}'
            power = random.randint(1, 20)
            type = random.randint(1, 20)
            cursor.execute("""INSERT INTO Engines(engine, power, type)
               VALUES(?, ?, ?);""", (engine_name, power, type))
        sqlite_connection.commit()
    except Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


create_db()
