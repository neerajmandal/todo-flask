from todo import Todo
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

    todo = Todo(item, todoType)

    todo_list.append(todo)
    return redirect('/')

@app.route('/move/<item>')
def move(item):
    progress_list.append(item)
    return redirect('/')

@app.route('/move1/<item>')
def move1(item):
    done_list.append(item)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)