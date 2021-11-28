import sqlite3
import os

class Database :
    def __init__(self,name):
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



database = Database(name="analitics")

