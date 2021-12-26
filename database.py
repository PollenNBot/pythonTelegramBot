import sqlite3
import os


class Datebase :
    def __init__(self, name):
        self.name = name
        self.connection = self.connect()

    def connect(self):
        db_path = os.path.join(os.getcwd(), f"{self.name}.db")
        if not os.path.exists(db_path):
            self.create_db()
        return sqlite3.connect(f"{self.name}.db")

    def create_db(self):
        connection = sqlite3.connect(f"{self.name}.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE all_analytics
                          (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                           event_date VARCHAR(30) NOT NULL,
                           event_data TEXT NOT NULL);''' )
        connection.commit()
        cursor.close()


    async def insert_all_analytics(self, event_date:str , event_data:str):
        cursor = self.connection.cursor()
        query = f"""INSERT INTO all_analytics(event_date, event_data) VALUES("{event_date}", "{event_data}")"""
        cursor.execute(query)
        self.connection.commit()
        cursor.close()


    async def select_all_analytics(self):
        cursor = self.connection.cursor()
        query = f'''SELECT event_date FROM all_analytics'''
        cursor.execute(query)
        records = cursor.fetchone()
        cursor.close()
        return records[0]

        
        






database = Datebase(name="analitics")