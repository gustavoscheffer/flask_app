# Flask Todo Application

A modular Flask web application for managing todo tasks with a clean, maintainable architecture following best practices.

## Features

- ✅ Create, read, update, and delete todos
- ✅ Mark todos as complete/incomplete
- ✅ SQLite database for data persistence
- ✅ Modular architecture with blueprints
- ✅ Application factory pattern
- ✅ Environment-based configuration
- ✅ Responsive web interface

## Project Structure

```
flask_app/
├── app/
│   ├── __init__.py          # Application factory
│   ├── config.py            # Configuration classes
│   ├── extensions.py        # Flask extensions
│   ├── models/              # Database models
│   │   ├── __init__.py
│   │   └── todo.py          # Todo model
│   ├── routes/              # Application routes
│   │   ├── __init__.py
│   │   └── main.py          # Main blueprint routes
│   ├── services/            # Business logic layer
│   │   ├── __init__.py
│   │   └── todo_service.py  # Todo service
│   └── templates/           # Jinja2 templates
│       ├── base.html
│       └── index.html
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   ├── test_config.py       # Configuration tests
│   ├── test_models.py       # Model tests
│   └── test_routes.py       # Route and integration tests
├── instance/                # Instance-specific files (SQLite DB)
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
├── pytest.ini               # Pytest configuration
├── .coveragerc              # Coverage configuration
├── .gitignore               # Git ignore rules
└── README.md
```

## Requirements

- Python 3.7+
- pip
- virtualenv (recommended)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd flask_app
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables (optional)

Create a `.env` file in the project root:

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///test.db
```

## Configuration

The application supports multiple configurations:

- **Development** (`development`) - Debug mode enabled, detailed error pages
- **Production** (`production`) - Optimized for production deployment
- **Testing** (`testing`) - Separate test database, testing mode enabled

Set the environment using the `FLASK_ENV` variable:

```bash
export FLASK_ENV=development  # or production, testing
```

## Running the Application

### Development Server

```bash
python run.py
```

Or using Flask CLI:

```bash
flask --app run run --debug
```

The application will be available at `http://127.0.0.1:5000`

### Production Server

For production, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
```

## Usage

### Adding a Todo

1. Navigate to the home page
2. Enter a task title in the input field
3. Click "Add" or press Enter

### Completing a Todo

Click the checkbox or "Complete" button next to a todo item to toggle its status.

### Deleting a Todo

Click the "Delete" button next to a todo item to remove it permanently.

## Development

### Database Migrations

The database is automatically created when you first run the application. To reset the database:

```bash
rm instance/test.db
python run.py
```

### Project Architecture

This application follows a modular architecture with clear separation of concerns:

- **Application Factory Pattern**: Enables multiple app instances for testing
- **Blueprints**: Organizes routes into logical modules
- **Service Layer**: Business logic separated from route handlers
- **Package-based Organization**: Models, routes, and services in dedicated directories
- **Extensions Module**: Centralized Flask extension initialization
- **Configuration Classes**: Environment-specific settings management

### Adding New Features

1. **Models**: Add database models to `app/models/` directory (e.g., `app/models/user.py`)
2. **Routes**: Add routes to `app/routes/` or create new blueprints (e.g., `app/routes/api.py`)
3. **Services**: Add business logic to `app/services/` (e.g., `app/services/user_service.py`)
4. **Templates**: Add HTML templates to `app/templates/`
5. **Configuration**: Update settings in `app/config.py`

**Example - Adding a new model:**
```python
# app/models/user.py
from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

# Update app/models/__init__.py
from app.models.user import User
__all__ = ['Todo', 'User']
```

## API Endpoints

| Method | Endpoint | Description |
|he application includes a comprehensive test suite covering models, routes, configuration, and integration scenarios.

### Test Structure

```
tests/
├── conftest.py          # Pytest fixtures and configuration
├── test_config.py       # Configuration tests (6 tests)
├── test_models.py       # Database model tests (14 tests)
└── test_routes.py       # Route and integration tests (21 tests)
```

### Running Tests

**Run all tests:**
```bash
pytest
```

**Run with verbose output:**
```bash
pytest -v
```

**Run with coverage report:**
```bash
pytest --cov=app --cov-report=html
```

**Run specific test file:**
```bash
pytest tests/test_models.py
```

**Run specific test:**
```bash
pytest tests/test_routes.py::TestRoutes::test_add_todo -v
```

**Run tests by marker:**
```bash
pytest -m unit          # Run unit tests only
pytest -m integration   # Run integration tests only
```

### Test Coverage

The test suite provides comprehensive coverage:

- **Configuration Tests**: Environment settings, configuration inheritance
- **Model Tests**: CRUD operations, validation, model methods
- **Route Tests**: All endpoints, edge cases, error handling
- **Integration Tests**: Complete workflows from add to delete

View detailed coverage report:
```bash
pytest --cov=app --cov-report=html
open htmlcov/index.html  # Opens coverage report in browser
```

### Writing New Tests

When adding new features, include tests in the appropriate test file:

1. **Models**: Add tests to `tests/test_models.py`
2. **Routes**: Add tests to `tests/test_routes.py`
3. **Configuration**: Add tests to `tests/test_config.py`

Use the fixtures in `tests/conftest.py`:
- `client`: Test client for HTTP requests
- `db`: Test database instance
- `sample_todo`: Single test todo
- `multiple_todos`: Multiple test todos

Example test:
```python
def test_my_feature(client, db):
    """Test my new feature."""
    response = client.post('/my-endpoint', data={'key': 'value'})
    assert response.status_code == 200
```

### Continuous Integration

Tests should be run before each commit and in CI/CD pipelines:

```bash
# Pre-commit testing
pytest --cov=app --cov-report=term-missing

# Ensure all tests pass before pushing
git commit -m "Your message" && pytest && git pushe/<id>` | Delete a todo |

## Testing

To run tests (when implemented):

```bash
export FLASK_ENV=testing
python -m pytest
```

## Deployment

### Environment Variables

Ensure these variables are set in production:

- `FLASK_ENV=production`
- `SECRET_KEY=<strong-secret-key>`
- `DATABASE_URL=<production-database-url>`

### Security Checklist

- [ ] Set a strong `SECRET_KEY`
- [ ] Use HTTPS in production
- [ ] Configure proper CORS policies
- [ ] Enable CSRF protection
- [ ] Use environment variables for sensitive data
- [ ] Update dependencies regularly

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask documentation and community
- SQLAlchemy for database ORM
- Contributors and maintainers

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

---

**Built with ❤️ using Flask**
