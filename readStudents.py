from conn import DatabaseConnection

db = DatabaseConnection(user="admin", password="admin", host
="localhost", port="5432", database="uptamca_db")
db.connect()
conexion = db.connection
cursor = db.cursor

#crear sentencia sql
sql = 'SELECT * FROM students ORDER BY id ASC;'

#ejecutar sentencia sql
cursor.execute(sql)

#recuperar los datos
registros = cursor.fetchall()

#recorrer los registros
for registro in registros:
    print(registro)
    
#cerrar la conexión
db.close()