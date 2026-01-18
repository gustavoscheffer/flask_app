"""Tests for database models."""
import pytest
from app.models import Todo
from app.extensions import db


class TestTodoModel:
    """Test Todo model."""
    
    def test_create_todo(self, db):
        """Test creating a new todo."""
        todo = Todo(title='Test Task')
        db.session.add(todo)
        db.session.commit()
        
        assert todo.id is not None
        assert todo.title == 'Test Task'
        assert todo.completed is False
    
    def test_todo_defaults(self, db):
        """Test todo default values."""
        todo = Todo(title='Default Test')
        db.session.add(todo)
        db.session.commit()
        
        assert todo.completed is False
    
    def test_todo_completed_status(self, db):
        """Test setting todo as completed."""
        todo = Todo(title='Complete Me', completed=True)
        db.session.add(todo)
        db.session.commit()
        
        assert todo.completed is True
    
    def test_todo_repr(self, sample_todo):
        """Test todo string representation."""
        repr_str = repr(sample_todo)
        assert 'Todo' in repr_str
        assert str(sample_todo.id) in repr_str
        assert sample_todo.title in repr_str
    
    def test_todo_to_dict(self, sample_todo):
        """Test todo to_dict method."""
        todo_dict = sample_todo.to_dict()
        
        assert isinstance(todo_dict, dict)
        assert 'id' in todo_dict
        assert 'title' in todo_dict
        assert 'completed' in todo_dict
        assert todo_dict['title'] == 'Test Todo'
        assert todo_dict['completed'] is False
    
    def test_query_todos(self, multiple_todos, db):
        """Test querying todos."""
        todos = Todo.query.all()
        assert len(todos) == 3
    
    def test_filter_completed_todos(self, multiple_todos, db):
        """Test filtering completed todos."""
        completed = Todo.query.filter_by(completed=True).all()
        incomplete = Todo.query.filter_by(completed=False).all()
        
        assert len(completed) == 1
        assert len(incomplete) == 2
    
    def test_update_todo(self, sample_todo, db):
        """Test updating a todo."""
        sample_todo.title = 'Updated Title'
        sample_todo.completed = True
        db.session.commit()
        
        updated_todo = Todo.query.get(sample_todo.id)
        assert updated_todo.title == 'Updated Title'
        assert updated_todo.completed is True
    
    def test_delete_todo(self, sample_todo, db):
        """Test deleting a todo."""
        todo_id = sample_todo.id
        db.session.delete(sample_todo)
        db.session.commit()
        
        deleted_todo = Todo.query.get(todo_id)
        assert deleted_todo is None
    
    def test_todo_title_required(self, db):
        """Test that todo title is required."""
        todo = Todo(title=None)
        db.session.add(todo)
        
        with pytest.raises(Exception):
            db.session.commit()
