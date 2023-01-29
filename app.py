from todo import Todo
import uuid
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

todo_list = []
progress_list = []
done_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list, progress_list=progress_list, done_list=done_list)

@app.route('/add', methods=['POST'])
def add():

    item = request.form['item']
    todoType = request.form['todoType']
    id = uuid.uuid1()

    todo = Todo(id, item, todoType)

    todo_list.append(todo)
    return redirect('/')

@app.route('/move/<id>')
def move(id):
    todo = searchList(id, todo_list)
    todo_list.remove(todo)
    progress_list.append(todo)
    return redirect('/')

@app.route('/move1/<id>')
def move1(id):
    todo = searchList(id, progress_list)
    progress_list.remove(todo)
    done_list.append(todo)
    return redirect('/')

def searchList(id, taskList):

    for task in taskList:
        if task.id == id:
            break

    return task

if __name__ == '__main__':
    app.run(debug=True)