from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        new_todo = Todo(title=title)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

# create a route to delete a todo by id
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    todo = Todo.query.get(id)
    if todo:
        db.session.delete(todo)
     
        db.session.commit()
    return redirect(url_for('index'))

#create a route to update a todo by id
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    todo = Todo.query.get(id)
    if todo:
        todo.completed = not todo.completed
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)