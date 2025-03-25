# CRUD con Python y psycopg2

Este proyecto es una implementación de un CRUD (Crear, Leer, Actualizar, Eliminar) utilizando Python y la librería `psycopg2` para conectarse a una base de datos SQL.

## Requisitos

- Python 3.x
- psycopg2
- Una base de datos PostgreSQL

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando:
    ```
    pip install psycopg2
    ```

## Configuración

1. Crea una base de datos PostgreSQL.
2. Configura las credenciales de la base de datos con el archivo `conn.py` con el Método `DatabaseConnection`:
    ```python
    Ejemplo de uso:
        db = DatabaseConnection(user="[user]", password="[admin]", host="[host]", port="5432", database="[name_db]")
    ```
