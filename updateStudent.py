from conn import DatabaseConnection

db = DatabaseConnection(user="admin", password="admin", host
="localhost", port="5432", database="uptamca_db")
db.connect()
conexion = db.connection
cursor = db.cursor

sql = 'UPDATE students SET name = %s, last_name = %s, date_birth = %s WHERE id = %s;'

# Solicitud de datos
id = input("Ingrese el id del estudiante: ")
name = input("Ingrese el nombre del estudiante: ")
last_name = input("Ingrese el apellido del estudiante: ")
date_birth = input("Ingrese la fecha de nacimiento del estudiante: formato (YYYY-MM-DD) ")
datos = (name, last_name, date_birth, id)
# Ejecutar la sentencia SQL
cursor.execute(sql, datos)

# Confirmar la transacción
conexion.commit()
print("Estudiante actualizado correctamente")

result = cursor.rowcount
print(f"Se actualizaron {result} registros")

# Cerrar la conexión
db.close()