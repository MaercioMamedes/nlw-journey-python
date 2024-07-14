import sqlite3
import os
from sqlite3 import Connection


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = ":memory:"
        self.__conn = None

    def connect(self) -> None:
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        cursor = conn.cursor()

        def execute_sql_file(sql_file_path_reference):
            with open(sql_file_path_reference, 'r') as sql_file:
                sql_string = sql_file.read()
                cursor.executescript(sql_string)
                conn.commit()
                print("rodou")
        dirname = os.path.dirname(os.path.realpath(__name__))
        sql_file_path = dirname + '/init/schema.sql'
        # sql_file_path = "/home/maercio/PROJETOS/nlw-journey-python/init/schema.sql"

        execute_sql_file(sql_file_path)

        self.__conn = conn

    def get_connection(self) -> Connection:
        return self.__conn


db_connection_handler_mock = DbConnectionHandler()
