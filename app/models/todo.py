"""Todo model."""
from app.extensions import db


class Todo(db.Model):
    """Todo model for task management."""
    
    __tablename__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        """String representation of Todo."""
        return f'<Todo {self.id}: {self.title}>'
    
    def to_dict(self):
        """Convert model to dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
