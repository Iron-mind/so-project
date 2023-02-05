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
        "host": "myhost",
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
def create_task():
 if not request.json :
  abort(400)
 count = request.json['count']
 cursor = conexion.cursor()
 cursor.execute("INSERT INTO counter (id, count) VALUES (1, %s)", (count,))
 res = cursor.fetchone()
 cursor.close()
 return jsonify({'response': res}), 201

# FIN - codigo comentado 4

# INICIO - codigo comentado 5
# Las siguientes lineas de codigo contienen las instrucciones para modificar 
# los datos de una tarea y de borrar una tarea dado un 'task_id'
#
'''
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
'''
# FIN - codigo comentado 5

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)