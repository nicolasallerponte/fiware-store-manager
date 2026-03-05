# System Architecture

## Overview

The Fiware Smart Store is built as a monolithic web application leveraging the Flask framework and a SQLite database. It follows a standard Model-View-Controller (MVC) architectural pattern, adapted for Flask's Blueprint routing and Jinja2 templating system. Multilingual UI support is handled using the Flask-Babel extension.

## Technology Stack

- **Web Framework:** Flask 3.x
- **Language:** Python 3.x
- **Database ORM:** SQLAlchemy (Flask-SQLAlchemy)
- **Database Engine:** SQLite (suitable for prototyping and local development)
- **Frontend Template Engine:** Jinja2
- **Styling:** Vanilla CSS3 (Custom Design System)
- **Internationalization (i18n):** Flask-Babel (PyBabel)

## Directory Structure

```
fiware-smart-store/
├── app/
│   ├── __init__.py          # App factory, DB and Babel initialization
│   ├── models.py            # SQLAlchemy database models
│   ├── routes/              # Blueprint controllers
│   │   ├── __init__.py      # Blueprint registration
│   │   ├── main.py          # Dashboard routes and locale switcher
│   │   ├── products.py      # Product specific routes
│   │   └── stores.py        # Store specific routes
│   ├── static/              # Static assets
│   │   └── css/
│   │       └── style.css    # Dark minimalist design system
│   └── templates/           # Jinja2 HTML templates
│       ├── base.html        # Main layout wrapper
│       ├── dashboard.html   # Main index view
│       ├── products/        # Product views
│       │   ├── detail.html
│       │   └── index.html
│       └── stores/          # Store views
│           ├── detail.html
│           └── index.html
├── docs/                    # Technical documentation
├── translations/            # .po/.mo translation files for EN, ES, GL, DE
├── tests/                   # Pytest test suite
│   ├── conftest.py          # Shared fixtures (app, db_session)
│   ├── test_models.py       # Unit tests for SQLAlchemy models
│   └── test_routes.py       # Integration tests for Flask routes
├── babel.cfg                # Babel extraction configuration
...
└── run.py                   # Application entry point
```

## Testing Strategy

The application employs a robust testing strategy using `pytest`:

1.  **Isolation:** Tests use an in-memory SQLite database (`sqlite:///:memory:`) to ensure speed and a clean state for every test run.
2.  **Fixtures:** Shared fixtures in `tests/conftest.py` provide a pre-configured Flask test client and a SQLAlchemy database session.
3.  **Model Testing:** Validates that data entities can be created, persisted, and that relationships (like cascade deletes) behave as expected.
4.  **Route Testing:** Verifies that all endpoints return the intended HTTP status codes and render data correctly from the database.

## Routing Strategy

The application uses Flask Blueprints to separate concerns into logical modules:

1. `main_bp`: Handles root-level endpoints like the Dashboard overview and the locale switching route.
2. `stores_bp`: Mounted at `/stores`. Handles listing all stores and serving detailed inventory views per store.
3. `products_bp`: Mounted at `/products`. Handles the master list of products and showing cross-store availability for specific items.

## Database Strategy

A relational SQLite database is used for data persistence. `Flask-SQLAlchemy` bridges the object-oriented Python models to the underlying SQL structure. The models enforce a Many-to-Many relationship between Stores and Products via an associative junction table `InventoryItem`, allowing localized stock tracking.

## Internationalization Strategy

Flask-Babel provides internationalization. The default language is set via user session or Accept-Language headers. Translations are stored in `.po` and `.mo` format inside the root `/translations` folder and can be extracted via Babel commands running atop `babel.cfg`.
