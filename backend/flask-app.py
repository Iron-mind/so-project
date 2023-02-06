#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request

"""
    Conexión a PostgreSQL con Python

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


app = Flask(__name__)

@app.route('/counter')
def index():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM counter where id=1")
    rows = cursor.fetchall()
    cursor.close()
    print(rows)
    return jsonify({'counter': rows[0][1]})

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

@app.route('/counter/<int:counter_id>', methods=['DELETE'])
def delete_task(counter_id):
    cursor = conexion.cursor()
    cursor.execute("UPDATE counter SET count = 0 WHERE id = 1")
    cursor.close()
    return jsonify({'result': "reset successful"})


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)