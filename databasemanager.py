import mysql.connector


class DatabaseManager:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="B33558800@k",
            database="shopping_db"
        )

        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query):
        self.cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            return self.cursor.fetchall()

        self.connection.commit()
        return True
    def execute_insert(self, query):
       self.cursor.execute(query)
       self.connection.commit()
       return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.connection.close()
