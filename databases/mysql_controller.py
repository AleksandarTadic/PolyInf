import pymysql
from .datatypes.datatypes import Datatypes
from .interfaces.idatabase_controller import IDatabaseController
from .db_connections.mysql_connection import MySQLConnection

import time

class MySQLController(IDatabaseController):
    def __init__(self, credentials) -> None:
        self.credentials = credentials
        
        self.connection = MySQLConnection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])




    def use_database(self, current_cursor, database_name):\
        current_cursor.execute("USE {}".format(database_name))


    def get_all(self, table_name, columns=None, values=None):
        data = []
        self.connection = MySQLConnection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
        try:
            with self.connection.cursor() as cursor:
                # sql = "USE {}".format(self.credentials["database"])
                # cursor.execute(sql)
                self.use_database(cursor, self.credentials["database"])
                if columns == None or values == None:
                    sql = "Select * FROM " + table_name
                    cursor.execute(sql)
                    # return cursor.fetchall()
                    data = cursor.fetchall()
                else:
                    sql = "SELECT * FROM " + table_name + " WHERE "
                    sql_values = []
                    for index, column in enumerate(columns):
                        if str(values[index]).strip() == "":
                            continue
                        if index > 0 and index < len(columns):
                            sql += " AND "
                        sql += column + " = " + "%s"
                        sql_values.append(str(values[index]))
                    cursor.execute(sql, sql_values)
                    data = cursor.fetchall()
                    # return cursor.fetchall()
        except (pymysql.Error, pymysql.Warning) as e:
            print(f'error! {e}')
        finally:
            MySQLConnection.close_connection()
        return data



    def get_one(self, table_name, columns, values):
        data = {}
        self.connection = MySQLConnection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
        try:
            with self.connection.cursor() as cursor:
                # sql = "USE {}".format(self.credentials["database"])
                # cursor.execute(sql)
                self.use_database(cursor, self.credentials["database"])
                sql = "SELECT * FROM " + table_name + " WHERE "
                sql_values = []
                for index, column in enumerate(columns):
                    if values[index].strip() == "":
                        continue
                    if index > 0 and index < len(columns):
                        sql += " AND "
                    sql += column + " = " + "%s"
                    sql_values.append(str(values[index]))
                cursor.execute(sql, sql_values)
                # return cursor.fetchone()
                data = cursor.fetchone()
        except (pymysql.Error, pymysql.Warning) as e:
            print(f'error! {e}')
        finally:
            MySQLConnection.close_connection()
        return data

    def insert(self, table_name, columns, values):
        self.connection = MySQLConnection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
        try:
            with self.connection.cursor() as cursor:
                # sql = "USE {}".format(self.credentials["database"])
                # cursor.execute(sql)
                self.use_database(cursor, self.credentials["database"])
                sql = "INSERT INTO " + table_name + "("  # (name, address) VALUES (%s, %s)"
                first = False
                for index, column in enumerate(columns):
                    if values[index].strip() == "":
                        continue
                    if first:
                        sql += ", "
                    sql += column
                    first = True
                sql += ") VALUES ("
                first = False
                for index, v in enumerate(values):
                    if v.strip() == "":
                        continue
                    if first:
                        sql += ", "
                    sql += "%s"
                    first = True
                sql += ")"
                values = tuple([v for v in values if v != ""])
                show_columns = cursor.execute("SHOW COLUMNS from {}".format(table_name))
                types = [column for column in show_columns(self.credentials["database"], table_name)]
                values = Datatypes.datatypes.sql_to_python(values, types)
                cursor.execute(sql, values)
        except (pymysql.Error, pymysql.Warning) as e:
            print(f'error! {e}')
        finally:
            MySQLConnection.close_connection()

    def update(self, table_name, columns, values):
        self.connection = MySQLConnection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
        try:
            with self.connection.cursor() as cursor:
                # sql = "USE {}".format(self.credentials["database"])
                # cursor.execute(sql)
                self.use_database(cursor, self.credentials["database"])
                sql = "UPDATE " + table_name + " SET "
                sql_values = []
                for index, column in enumerate(columns):
                    if index > 0 and index < len(columns):
                        sql += ", "
                    sql += column + " = " + "%s"
                    sql_values.append(str(values[index]))
                sql += " WHERE "
                show_columns = cursor.execute("SHOW COLUMNS from {}".format(table_name))
                columns_data = [column for column in show_columns(
                    self.credentials["database"], table_name)]
                first = False
                for index, column in enumerate(columns_data):
                    if column[3] == "PRI":
                        if first and index > 0 and index < len(columns_data):
                            sql += ", "
                        sql += columns[index] + " = " + "%s"
                        sql_values.append(str(values[index]))
                        first = True
                cursor.execute(sql, sql_values)
        except (pymysql.Error, pymysql.Warning) as e:
            print(f'error! {e}')
        finally:
            MySQLConnection.close_connection()

    def delete(self, table_name, columns):
        self.connection = MySQLConnection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
        try:
            with self.connection.cursor() as cursor:
                # sql = "USE {}".format(self.credentials["database"])
                # cursor.execute(sql)
                self.use_database(cursor, self.credentials["database"])
                sql = "DELETE FROM "+table_name+" WHERE "
                show_columns = cursor.execute("SHOW COLUMNS from {}".format(table_name))
                table_columns = [column for column in show_columns(
                    self.credentials["database"], table_name)]
                for index, column in enumerate(columns):
                    if index > 0 and index < len(columns):
                        sql += " AND "
                    sql += table_columns[index][0]+" = %s"
                val = tuple(columns)
                cursor.execute(sql, val)
        except (pymysql.Error, pymysql.Warning) as e:
            print(f'error! {e}')
        finally:
            MySQLConnection.close_connection()

    def personalni_zadatak(self, p1, p2, p3):
        data = []
        self.connection = MySQLConnection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
        try:
            with self.connection.cursor() as cursor:
                # sql = "USE {}".format(self.credentials["database"])
                # cursor.execute(sql)
                self.use_database(cursor, self.credentials["database"])
                # sql = "CALL DobaviPersonalniZadatak(%s, %s, %s)"
                # in_values = [p1, p2, p3]
                # cursor.execute(sql, in_values)
                cursor.callproc("DobaviPersonalniZadatak", [p1, p2, p3])
                data = cursor.fetchall()
        except (pymysql.Error, pymysql.Warning) as e:
            print(f'error! {e}')
        finally:
            MySQLConnection.close_connection()
        return data
    
    def personalni_zadatak_arango(self):
        data = []
        self.connection = MySQLConnection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
        try:
            with self.connection.cursor() as cursor:
                # sql = "USE {}".format(self.credentials["database"])
                # cursor.execute(sql)
                self.use_database(cursor, self.credentials["database"])
                # sql = "CALL DobaviPersonalniZadatak(%s, %s, %s)"
                # in_values = [p1, p2, p3]
                # cursor.execute(sql, in_values)
                cursor.callproc("TempTabelaArango", [])
                sql = "Select * FROM TempArango" 
                cursor.execute(sql)
                data = cursor.fetchall()
        except (pymysql.Error, pymysql.Warning) as e:
            print(f'error! {e}')
        finally:
            MySQLConnection.close_connection()
        return data
    
    # def personalni_zadatak_arango(self):
    #     data = []
    #     self.connection = MySQLConnection.get_connection(self.credentials["host"], self.credentials["port"], self.credentials["user"], self.credentials["password"])
    #     try:
    #         with self.connection.cursor() as cursor:
    #             # sql = "USE {}".format(self.credentials["database"])
    #             # cursor.execute(sql)
    #             self.use_database(cursor, self.credentials["database"])
    #             # sql = "CALL DobaviPersonalniZadatak(%s, %s, %s)"
    #             # in_values = [p1, p2, p3]
    #             # cursor.execute(sql, in_values)
    #             cursor.callproc("DobaviPersonalniZadatakArango", [])
    #             data = cursor.fetchall()
    #     except (pymysql.Error, pymysql.Warning) as e:
    #         print(f'error! {e}')
    #     finally:
    #         MySQLConnection.close_connection()
    #     return data