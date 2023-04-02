import mysql.connector
import logging
import config
from mysql.connector import Error

class Database():
    def __init__(self, host, database, user, passw):
        try:
            logging.basicConfig(filename=config.log_sql, encoding="utf-8", level=logging.DEBUG)
            self.conn = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=passw
            )

            self.cursor = self.conn.cursor()

            if self.conn.is_connected():
                print("Debug connected to mysql")

        except Error as e:
            logging.error(e)
            print(f"Error: {e}")
            self.close_conn()

    def execute_read(self, query):
        try:
            self.res = self.cursor.execute(query)

            return self.cursor.fetchall()
        
        except Error as e:
            logging.error(e)
            print(f"Error: {e}")
            self.close_conn()

    def callfc(self, func, args=None):
        try:
            if args:
                args = tuple(map(lambda x : f"'{x}'", args))
                query = f"SELECT {func}({', '.join(args)})"
                self.res = self.execute_read(query)
            else:
                self.res = self.execute_read(f"SELECT {func}()")

            self.conn.commit()
            return self.res
        
        except Error as e:
            logging.error(e)
            print(f"Error: {e}")
            self.close_conn()

    def callpr(self, pr, args=None):
        try:
            if args:
                self.res = self.cursor.callproc(pr, args=args)
            else:
                self.res = self.cursor.callproc(pr)

            self.conn.commit()
            return (
                self.res,
                self.cursor.fetchall()
            )
        
        except Error as e:
            logging.error(e)
            print(f"Error: {e}")
            self.close_conn()

    def close_conn(self):
        self.conn.close()
        return self