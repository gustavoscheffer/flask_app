"""Pytest configuration and fixtures."""
import os
import pytest
from app import create_app
from app.extensions import db as _db
from app.models import Todo


@pytest.fixture(scope='session')
def app():
    """Create and configure a test application instance."""
    # Create the app with testing configuration
    app = create_app('testing')
    
    # Create application context
    with app.app_context():
        yield app


@pytest.fixture(scope='function')
def db(app):
    """Create a test database for each test function."""
    with app.app_context():
        # Create all tables
        _db.create_all()
        
        yield _db
        
        # Clean up after test
        _db.session.remove()
        _db.drop_all()


@pytest.fixture(scope='function')
def client(app, db):
    """Create a test client for the app."""
    return app.test_client()


@pytest.fixture(scope='function')
def runner(app):
    """Create a test CLI runner."""
    return app.test_cli_runner()


@pytest.fixture
def sample_todo(db):
    """Create a sample todo for testing."""
    todo = Todo(title='Test Todo', completed=False)
    db.session.add(todo)
    db.session.commit()
    return todo


@pytest.fixture
def multiple_todos(db):
    """Create multiple todos for testing."""
    todos = [
        Todo(title='First Todo', completed=False),
        Todo(title='Second Todo', completed=True),
        Todo(title='Third Todo', completed=False),
    ]
    for todo in todos:
        db.session.add(todo)
    db.session.commit()
    return todos
