"""Application routes."""
from flask import Blueprint, render_template, request, redirect, url_for

from app.models import Todo
from app.extensions import db

# Create blueprint
main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Display all todos."""
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@main.route('/add', methods=['POST'])
def add():
    """Add a new todo."""
    title = request.form.get('title')
    
    if title:
        new_todo = Todo(title=title)
        db.session.add(new_todo)
        db.session.commit()
    
    return redirect(url_for('main.index'))


@main.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    """Delete a todo by id."""
    todo = Todo.query.get(id)
    
    if todo:
        db.session.delete(todo)
        db.session.commit()
    
    return redirect(url_for('main.index'))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    """Toggle a todo's completed status."""
    todo = Todo.query.get(id)
    
    if todo:
        todo.completed = not todo.completed
        db.session.commit()
    
    return redirect(url_for('main.index'))
