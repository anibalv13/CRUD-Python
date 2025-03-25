from conn import DatabaseConnection

db = DatabaseConnection(user="admin", password="admin", host
="localhost", port="5432", database="uptamca_db")
db.connect()
conexion = db.connection
cursor = db.cursor

sql = 'DELETE FROM students WHERE id = %s;'

# Solicitud de datos
id = input("Ingrese el id del estudiante a eliminar: ")
datos = (id,)
# Ejecutar la sentencia SQL
cursor.execute(sql, datos)

# Confirmar la transacción
conexion.commit()
print("Estudiante eliminado correctamente")

result = cursor.rowcount
print(f"Se eliminaron {result} registros")

# Cerrar la conexión
db.close()