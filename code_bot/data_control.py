import sqlite3 as sl
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sl.connect(path, check_same_thread=False)
        print("Подключение к базе данных SQLite прошло успешно")
    except Error as e:
        print(f"Произошла ошибка '{e}'")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запрос выполнен успешно")
        try:
            return cursor.fetchall()
        except:
            ...
    except Error as e:
        print(f"Произошла ошибка'{e}'")


def execute_many_query(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("Запрос выполнен успешно")
    except Error as e:
        print(f"Произошла ошибка '{e}'")


def create_table(connection):
    create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
          user_id TEXT NOT NULL,
          name TEXT NOT NULL,
          date INEGER
        );
        """
    execute_query(connection, create_users_table)


def create_record(connection, user_id, name, date):
    data = [(user_id, name, date)]
    request_to_create = 'INSERT INTO users (user_id, name, date) VALUES (?, ?, ?)'
    execute_many_query(connection, request_to_create, data)


def get_records(connection):
    request_to_get = 'SELECT * FROM users'
    info = execute_query(connection, request_to_get)
    return info
