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
│   ├── models.py            # Database models
│   └── routes.py            # Application routes
├── instance/                # Instance-specific files (SQLite DB)
├── templates/               # Jinja2 templates
│   ├── base.html
│   └── index.html
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
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

This application follows a modular architecture:

- **Application Factory Pattern**: Enables multiple app instances for testing
- **Blueprints**: Organizes routes into logical modules
- **Extensions Module**: Centralized Flask extension initialization
- **Configuration Classes**: Environment-specific settings management

### Adding New Features

1. **Models**: Add database models to `app/models.py`
2. **Routes**: Add routes to `app/routes.py` or create new blueprints
3. **Templates**: Add HTML templates to `templates/`
4. **Configuration**: Update settings in `app/config.py`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Display all todos |
| POST | `/add` | Create a new todo |
| POST | `/update/<id>` | Toggle todo completion status |
| POST | `/delete/<id>` | Delete a todo |

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
