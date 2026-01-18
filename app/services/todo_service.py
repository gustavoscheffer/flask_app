"""Business logic services for the application."""
from typing import List, Optional
from app.models import Todo
from app.extensions import db


class TodoService:
    """Service class for Todo business logic."""
    
    @staticmethod
    def get_all_todos() -> List[Todo]:
        """
        Retrieve all todos from the database.
        
        Returns:
            List of all Todo objects
        """
        return Todo.query.all()
    
    @staticmethod
    def get_todo_by_id(todo_id: int) -> Optional[Todo]:
        """
        Retrieve a single todo by its ID.
        
        Args:
            todo_id: The ID of the todo to retrieve
            
        Returns:
            Todo object if found, None otherwise
        """
        return Todo.query.get(todo_id)
    
    @staticmethod
    def create_todo(title: str) -> Optional[Todo]:
        """
        Create a new todo with the given title.
        
        Args:
            title: The title of the new todo
            
        Returns:
            Created Todo object if title is valid, None otherwise
        """
        if not title or not title.strip():
            return None
        
        new_todo = Todo(title=title.strip())
        db.session.add(new_todo)
        db.session.commit()
        return new_todo
    
    @staticmethod
    def delete_todo(todo_id: int) -> bool:
        """
        Delete a todo by its ID.
        
        Args:
            todo_id: The ID of the todo to delete
            
        Returns:
            True if todo was deleted, False if todo not found
        """
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return False
        
        db.session.delete(todo)
        db.session.commit()
        return True
    
    @staticmethod
    def toggle_todo_completion(todo_id: int) -> Optional[Todo]:
        """
        Toggle the completion status of a todo.
        
        Args:
            todo_id: The ID of the todo to update
            
        Returns:
            Updated Todo object if found, None otherwise
        """
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return None
        
        todo.completed = not todo.completed
        db.session.commit()
        return todo
    
    @staticmethod
    def update_todo(todo_id: int, title: Optional[str] = None, 
                   completed: Optional[bool] = None) -> Optional[Todo]:
        """
        Update a todo's properties.
        
        Args:
            todo_id: The ID of the todo to update
            title: New title (optional)
            completed: New completion status (optional)
            
        Returns:
            Updated Todo object if found, None otherwise
        """
        todo = Todo.query.get(todo_id)
        
        if not todo:
            return None
        
        if title is not None and title.strip():
            todo.title = title.strip()
        
        if completed is not None:
            todo.completed = completed
        
        db.session.commit()
        return todo
