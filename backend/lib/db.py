"""
    Conexión a PostgreSQL con Python
    Ejemplo de CRUD evitando inyecciones SQL
    
    @author parzibyte
    Más tutoriales en:
                        parzibyte.me/blog
"""

import psycopg2
try:
    credenciales = {
        "dbname": "proyectoso",
        "user": "admin",
        "password": "pg1234",
        "host": "dbhost",
        "port": 5433
    }
    conexion = psycopg2.connect(**credenciales)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)