from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task list
tasks = []

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# POST a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Task must have a title'}), 400
    task = {'id': len(tasks) + 1, 'title': data['title']}
    tasks.append(task)
    return jsonify(task), 201

# DELETE a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': f'Task {task_id} deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)