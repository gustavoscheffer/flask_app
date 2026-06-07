# Todo App

A modular Flask web application for managing todo tasks with a clean, maintainable architecture.

## Features

- ✅ Create, view, update, and delete todo items
- ✅ Mark todos as complete or incomplete
- ✅ SQLite persistence with SQLAlchemy
- ✅ Application factory pattern for easy testing
- ✅ Blueprint-based route organization
- ✅ Service layer for business logic separation

## Project Structure

```
todo_app/
├── app/
│   ├── __init__.py          # Application factory and initialization
│   ├── config.py            # Configuration classes
│   ├── extensions.py        # Flask extension initialization
│   ├── models/              # Database models
│   │   ├── __init__.py
│   │   └── todo.py          # Todo model
│   ├── routes/              # Application blueprints and routes
│   │   ├── __init__.py
│   │   └── main.py          # Main routes
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
├── Dockerfile               # Optional container build
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
├── pytest.ini               # Pytest configuration
└── todo_app_dep.yaml        # Dependency metadata
```

## Requirements

- Python 3.7+
- pip
- virtualenv (recommended)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd todo_app
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The app supports the following environments:

- `development` - Debug mode enabled
- `production` - Production-ready settings
- `testing` - Testing mode with a separate database

The environment is selected with `FLASK_ENV`:

```bash
export FLASK_ENV=development
```

Optional configuration variables:

```bash
export SECRET_KEY=your-secret-key
export DATABASE_URL=sqlite:///test.db
```

## Running the Application

Start the app locally:

```bash
python run.py
```

Then open `http://127.0.0.1:5000` in your browser.

### Production Server

Use Gunicorn for production hosting:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
```

## Usage

- Add a todo by entering a task title and clicking **Add**.
- Toggle completion status using the checkbox.
- Delete todos using the **Delete** button.

## Testing

Run the test suite with pytest:

```bash
pytest
```

## Notes

- The app uses SQLAlchemy with SQLite by default.
- The database files are created automatically when the app starts.
- `run.py` builds the app using `app.create_app()` and runs it in debug mode by default.

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
