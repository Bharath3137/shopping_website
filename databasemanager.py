import mysql.connector
class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect()
        self.cursor = self.connection.cursor(dictionary=True)
        host="localhost",
        user="root",
        password="B33558800@k",
        database="shopping_db"

    def execute_query(self, query):
        self.cursor.execute(query)
    def close(self):
        self.cursor.close()
        self.connection.close()
        
       
