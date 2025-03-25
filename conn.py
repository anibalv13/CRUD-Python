import psycopg2

class DatabaseConnection:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(user=self.user,
                                               password=self.password,
                                               host=self.host,
                                               port=self.port,
                                               database=self.database)
            self.cursor = self.connection.cursor()
            print("Connection successful")
        except Exception as error:
            print(f"Error connecting to database: {error}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed")

# Ejemplo de uso:
# db = DatabaseConnection(user="admin", password="admin", host="localhost", port="5432", database="uptamca_db")
# db.connect()
# # Realizar operaciones en la base de datos
# db.close()