"""Tests for application routes."""
import pytest
from flask import url_for
from app.models import Todo


class TestRoutes:
    """Test application routes."""
    
    def test_index_route(self, client, db):
        """Test the index route."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'<!DOCTYPE html>' in response.data or b'<html' in response.data
    
    def test_index_shows_todos(self, client, multiple_todos):
        """Test that index page displays todos."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'First Todo' in response.data
        assert b'Second Todo' in response.data
        assert b'Third Todo' in response.data
    
    def test_index_empty_list(self, client, db):
        """Test index page with no todos."""
        response = client.get('/')
        assert response.status_code == 200
        # Should still render successfully even with no todos
    
    def test_add_todo(self, client, db):
        """Test adding a new todo."""
        response = client.post('/add', data={'title': 'New Todo'}, follow_redirects=True)
        assert response.status_code == 200
        
        # Verify todo was added to database
        todo = Todo.query.filter_by(title='New Todo').first()
        assert todo is not None
        assert todo.title == 'New Todo'
        assert todo.completed is False
    
    def test_add_todo_empty_title(self, client, db):
        """Test adding a todo with empty title."""
        initial_count = Todo.query.count()
        response = client.post('/add', data={'title': ''}, follow_redirects=True)
        assert response.status_code == 200
        
        # Verify no todo was added
        assert Todo.query.count() == initial_count
    
    def test_add_todo_missing_title(self, client, db):
        """Test adding a todo without title field."""
        initial_count = Todo.query.count()
        response = client.post('/add', data={}, follow_redirects=True)
        assert response.status_code == 200
        
        # Verify no todo was added
        assert Todo.query.count() == initial_count
    
    def test_delete_todo(self, client, sample_todo, db):
        """Test deleting a todo."""
        todo_id = sample_todo.id
        response = client.post(f'/delete/{todo_id}', follow_redirects=True)
        assert response.status_code == 200
        
        # Verify todo was deleted
        deleted_todo = Todo.query.get(todo_id)
        assert deleted_todo is None
    
    def test_delete_nonexistent_todo(self, client, db):
        """Test deleting a non-existent todo."""
        response = client.post('/delete/9999', follow_redirects=True)
        assert response.status_code == 200
        # Should handle gracefully without error
    
    def test_update_todo(self, client, sample_todo, db):
        """Test updating a todo's completion status."""
        todo_id = sample_todo.id
        initial_status = sample_todo.completed
        
        response = client.post(f'/update/{todo_id}', follow_redirects=True)
        assert response.status_code == 200
        
        # Verify status was toggled
        updated_todo = Todo.query.get(todo_id)
        assert updated_todo.completed == (not initial_status)
    
    def test_update_toggle_multiple_times(self, client, sample_todo, db):
        """Test toggling a todo multiple times."""
        todo_id = sample_todo.id
        
        # First toggle
        client.post(f'/update/{todo_id}')
        todo = Todo.query.get(todo_id)
        assert todo.completed is True
        
        # Second toggle
        client.post(f'/update/{todo_id}')
        todo = Todo.query.get(todo_id)
        assert todo.completed is False
        
        # Third toggle
        client.post(f'/update/{todo_id}')
        todo = Todo.query.get(todo_id)
        assert todo.completed is True
    
    def test_update_nonexistent_todo(self, client, db):
        """Test updating a non-existent todo."""
        response = client.post('/update/9999', follow_redirects=True)
        assert response.status_code == 200
        # Should handle gracefully without error
    
    def test_add_redirects_to_index(self, client, db):
        """Test that add route redirects to index."""
        response = client.post('/add', data={'title': 'Redirect Test'})
        assert response.status_code == 302
        assert '/' in response.location
    
    def test_delete_redirects_to_index(self, client, sample_todo):
        """Test that delete route redirects to index."""
        response = client.post(f'/delete/{sample_todo.id}')
        assert response.status_code == 302
        assert '/' in response.location
    
    def test_update_redirects_to_index(self, client, sample_todo):
        """Test that update route redirects to index."""
        response = client.post(f'/update/{sample_todo.id}')
        assert response.status_code == 302
        assert '/' in response.location


class TestIntegration:
    """Integration tests for complete workflows."""
    
    def test_complete_workflow(self, client, db):
        """Test a complete todo workflow: add, update, delete."""
        # Add a todo
        client.post('/add', data={'title': 'Workflow Test'})
        todo = Todo.query.filter_by(title='Workflow Test').first()
        assert todo is not None
        assert todo.completed is False
        
        # Mark as completed
        client.post(f'/update/{todo.id}')
        todo = Todo.query.get(todo.id)
        assert todo.completed is True
        
        # Delete the todo
        client.post(f'/delete/{todo.id}')
        todo = Todo.query.get(todo.id)
        assert todo is None
    
    def test_multiple_todos_workflow(self, client, db):
        """Test managing multiple todos."""
        # Add multiple todos
        titles = ['Task 1', 'Task 2', 'Task 3']
        for title in titles:
            client.post('/add', data={'title': title})
        
        assert Todo.query.count() == 3
        
        # Complete some todos
        todos = Todo.query.all()
        client.post(f'/update/{todos[0].id}')
        client.post(f'/update/{todos[2].id}')
        
        completed = Todo.query.filter_by(completed=True).count()
        incomplete = Todo.query.filter_by(completed=False).count()
        
        assert completed == 2
        assert incomplete == 1
        
        # Delete one todo
        client.post(f'/delete/{todos[1].id}')
        assert Todo.query.count() == 2
