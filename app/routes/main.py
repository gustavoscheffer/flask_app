"""Application routes."""
from flask import Blueprint, render_template, request, redirect, url_for

from app.services import TodoService

# Create blueprint
main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Display all todos."""
    todos = TodoService.get_all_todos()
    return render_template('index.html', todos=todos)


@main.route('/add', methods=['POST'])
def add():
    """Add a new todo."""
    title = request.form.get('title')
    TodoService.create_todo(title)
    return redirect(url_for('main.index'))


@main.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    """Delete a todo by id."""
    TodoService.delete_todo(id)
    return redirect(url_for('main.index'))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    """Toggle a todo's completed status."""
    TodoService.toggle_todo_completion(id)
    return redirect(url_for('main.index'))
