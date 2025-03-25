from conn import DatabaseConnection

db = DatabaseConnection(user="admin", password="admin", host
="localhost", port="5432", database="uptamca_db")
db.connect()
conexion = db.connection
cursor = db.cursor

sql = 'INSERT INTO students (name, last_name, date_birth) VALUES (%s, %s, %s);'

# Solicitud de datos
name = input("Ingrese el nombre del estudiante: ")
last_name = input("Ingrese el apellido del estudiante: ")
date_birth = input("Ingrese la fecha de nacimiento del estudiante: formato (YYYY-MM-DD) ")

datos = (name, last_name, date_birth)
# Ejecutar la sentencia SQL
cursor.execute(sql, datos)

# Confirmar la transacción
conexion.commit()
print("Estudiante insertado correctamente")

result = cursor.rowcount
print(f"Se insertaron {result} registros")

# Cerrar la conexión
db.close()

