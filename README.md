# Flask Todo Application

A simple todo list application built with Flask and SQLAlchemy, demonstrating basic CRUD operations.

## Features

- ✅ Add new todo items
- ✅ Mark todos as completed/uncompleted
- ✅ Delete todo items
- ✅ SQLite database for data persistence
- ✅ Clean and responsive UI

## Project Structure

```
.
├── app.py                # Main Flask application
├── wsgi.py              # WSGI entry point
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── app/                 # Application package
│   ├── __init__.py      # App initialization
│   ├── extensions.py    # Flask extensions
│   ├── forms.py         # Form definitions
│   ├── models.py        # Database models
│   ├── routes.py        # Route handlers
│   ├── services.py      # Business logic
│   ├── statics/         # Static files (CSS, JS, images)
│   └── templates/       # Jinja2 templates
│       ├── base.html    # Base template
│       └── index.html   # Main todo list page
├── instance/            # Instance-specific files (database)
├── migrations/          # Database migration scripts
└── tests/               # Test files
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd module_3
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python app.py
   ```

## Running the Application

### Development Mode

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`

### Using Flask CLI

```bash
export FLASK_APP=app.py  # On Windows: set FLASK_APP=app.py
flask run
```

## Usage

1. **Add a Todo**: Enter a task in the input field and click "Add" or press Enter
2. **Complete a Todo**: Click the "Complete" button or checkbox next to a todo item to toggle its status
3. **Delete a Todo**: Click the "Delete" button to remove a todo item

## Database

The application uses SQLite for data storage. The database file (`test.db`) is created in the `instance/` folder on first run.

### Todo Model

```python
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Display all todos |
| POST | `/add` | Add a new todo |
| POST | `/update/<id>` | Toggle todo completion status |
| POST | `/delete/<id>` | Delete a todo |

## Dependencies

- **Flask** (3.1.2) - Web framework
- **Flask-SQLAlchemy** (3.1.1) - ORM for database operations
- **SQLAlchemy** (2.0.45) - Database toolkit
- **Jinja2** (3.1.6) - Template engine
- **Werkzeug** (3.1.5) - WSGI utilities

See [requirements.txt](requirements.txt) for the complete list.

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Database Migrations

If using Flask-Migrate:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Troubleshooting

### "Failed to find Flask application or factory in module 'app'"

Make sure you're running the application using:
- `python app.py` (recommended for development)
- Or set the correct FLASK_APP: `export FLASK_APP=app.py && flask run`

### Database Issues

If you encounter database errors, delete the `instance/test.db` file and restart the application to recreate the database.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Contact

For questions or support, please open an issue in the repository.
