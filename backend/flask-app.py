#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request

"""
    Conexión a PostgreSQL con Python
    Ejemplo de CRUD evitando inyecciones SQL

"""

import psycopg2
conexion = None
try:
    credenciales = {
        "dbname": "proyectoso",
        "user": "admin",
        "password": "pg1234",
        "host": "dbhost",
        "port": 5432
    }
    conexion = psycopg2.connect(**credenciales)
    conexion.autocommit = True
    cursor = conexion.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print("Conectado a Postgre: ", row)
    cursor.execute("CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, count INTEGER); INSERT INTO counter (id, count) VALUES (1, 0) ON CONFLICT DO NOTHING;")
    cursor.close()

except psycopg2.Error as e:
  
    print("Ocurrió un error al conectar a PostgreSQL: ", e)

# cursor = conexion.cursor()

app = Flask(__name__)
# INICIO codigo comentado 
# FIN - codigo comentado 1

@app.route('/counter')
def index():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM counter")
    rows = cursor.fetchall()
    cursor.close()
    print(rows)
    return jsonify({'counter': rows})

@app.route('/counter', methods=['POST'])
def create_count():
  if not request.json :
        abort(400)
    count = request.json['count']
    cursor = conexion.cursor()
    cursor.execute("UPDATE counter SET count = %s WHERE id = 1", (count,))
    cursor.close()
    return jsonify({'response': "OK"})


@app.route('/counter', methods=['PUT'])
def update_counter():
    if not request.json :
        abort(400)
    count = request.json['count']
    cursor = conexion.cursor()
    cursor.execute("UPDATE counter SET count = %s WHERE id = 1", (count,))
    cursor.close()
    return jsonify({'response': "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)