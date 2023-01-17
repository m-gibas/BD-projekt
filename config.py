#!/usr/bin/python
from configparser import ConfigParser
import psycopg2

# funkcja do pozyskania danych potrzebnych do zalogowania się z bazą
def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

# funkcja do łączenia się z bazą
def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return 0

# funkcja do rozłączenia się z bazą
def disconnect(conn):
    if conn is not None:
        conn.close()