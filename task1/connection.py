import psycopg2
import os
from dotenv import load_dotenv


class Connection:
    def __init__(self):
        load_dotenv()

        self.__conn = psycopg2.connect(
            dbname=os.getenv('POSTGRES_DB_NAME'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('POSTGRES_HOST'),
            port=os.getenv('POSTGRES_PORT'),
        )

    def get_cursor(self):
        return self.__conn.cursor()

    def fetchall(self, sql):
        try:
            cursor = self.get_cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")

        return []  # TODO: is better to return None but I don't want to processing it when it will be used

    def commit(self):
        self.__conn.commit()
