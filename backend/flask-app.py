#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request
import 'lib/db.py' 
app = Flask(__name__)
# INICIO codigo comentado 1
'''
tasks = [
 {
  'id': 1,
  'title': "Buy groceries",
  'description': "Milk, cheese, pizaa",
  'done': False
 },
 {
  'id': 2,
  'title': "Learn Python",
  'description': "Need a good tutorial on the web",
  'done': False
 }
]
'''
# FIN - codigo comentado 1

@app.route('/')
def index():
    return "Hola, World!"

# INICIO codigo comentado 1
# Se habilita un endpoint para devolver todas las tareas almacenadas en la 
# variables 'tasks'
#
'''
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
 return jsonify({'tasks': tasks})
'''
# FIN - codigo comentado 1

# INICIO - codigo comentado 2
# Permite recuperar una tarea dado un 'task_id'
#
'''
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
 task = [task for task in tasks if task['id'] == task_id]
 if len(task) == 0:
  abort(404)
 return jsonify({'task': task[0]})
'''
# FIN - codigo comentado 2

# INICIO - codigo comentado 3
# Una forma de personalizar los errores arrojados por la aplicacion
#
'''
@app.errorhandler(404)
def not_found(error):
 return make_response(jsonify({'error': 'Not found'}), 404)
'''
# FIN - codigo comentado 3

# INICIO - codigo comentado 4
# Endpoint que permite la creacion de una nueva tarea a traves de la linea de
# comandos.
#
'''
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
 if not request.json or not 'title' in request.json:
  abort(400)
 task = {
  'id': tasks[-1]['id'] + 1,
  'title': request.json['title'],
  'description': request.json.get('description', ""),
  'done': False
 }
 tasks.append(task)
 return jsonify({'task': task}), 201
'''
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