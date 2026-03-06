# fiware-smart-store

A FIWARE-compliant smart supermarket management platform built with Flask and NGSIv2. Manages stores, products, shelves, inventory, and employees with full CRUD operations, multi-language support, and Orion Context Broker integration.

![Python](https://img.shields.io/badge/python-3.14-blue)
![Flask](https://img.shields.io/badge/flask-3.x-lightgrey)
![FIWARE](https://img.shields.io/badge/powered%20by-FIWARE-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Features

- **FIWARE NGSIv2** data model with URN-based entity IDs (`urn:ngsi-ld:EntityType:XXX`)
- **Orion Context Broker** integration with automatic SQLite fallback
- **Full CRUD** for inventory items and shelves via modal-based UI
- **Interactive maps** using Leaflet.js + OpenStreetMap in store detail views
- **Multi-language support**: English, Spanish, Galician, German (Flask-Babel)
- **Entities**: Store, Shelf, Product, InventoryItem, Employee
- **Docker Compose** setup for Orion + MongoDB

---

## Tech Stack

| Layer          | Technology                          |
| -------------- | ----------------------------------- |
| Backend        | Python 3.14, Flask, SQLAlchemy      |
| Database       | SQLite (default), MongoDB via Orion |
| Context Broker | FIWARE Orion NGSIv2                 |
| Frontend       | Jinja2, Leaflet.js, vanilla JS      |
| i18n           | Flask-Babel (gettext)               |
| Testing        | pytest, pytest-flask                |
| Infrastructure | Docker, Docker Compose              |

---

## Getting Started

### Prerequisites

- Python 3.10+
- Docker and Docker Compose
- `uv` or `pip`

### Installation

```bash
git clone https://github.com/nicolasallerponte/fiware-store-manager.git
cd fiware-store-manager
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configuration

Copy the example environment file and edit if needed:

```bash
cp .env.example .env
```

Default `.env`:

```
ORION_URL=http://localhost:1026
```

### Running with Orion (recommended)

```bash
./start.sh
```

This will:

1. Stop any running containers
2. Start Orion Context Broker + MongoDB via Docker Compose
3. Initialize the SQLite database with sample data
4. Start the Flask development server

### Running without Docker (SQLite only)

```bash
python init_db.py
python run.py
```

### Stopping

```bash
./stop.sh
```

---

## Project Structure

```
fiware-smart-store/
├── app/
│   ├── __init__.py         # App factory, Orion connectivity check
│   ├── models.py           # SQLAlchemy models (FIWARE NGSIv2)
│   ├── routes/             # Blueprints: stores, products, employees, main
│   ├── static/css/         # Stylesheet (light minimalist design)
│   └── templates/          # Jinja2 templates
├── docs/                   # PRD, architecture, data model
├── tests/                  # pytest test suite (14 tests)
├── translations/           # Flask-Babel .po/.mo files (en, es, gl, de)
├── docker-compose.yml      # Orion + MongoDB
├── init_db.py              # Sample data seeding
├── start.sh                # Start containers + app
├── stop.sh                 # Stop containers
└── requirements.txt
```

---

## Data Model

All entities follow the FIWARE NGSIv2 pattern with URN identifiers:

| Entity        | URN Pattern                     |
| ------------- | ------------------------------- |
| Store         | `urn:ngsi-ld:Store:XXX`         |
| Shelf         | `urn:ngsi-ld:Shelf:XXX`         |
| Product       | `urn:ngsi-ld:Product:XXX`       |
| InventoryItem | `urn:ngsi-ld:InventoryItem:XXX` |
| Employee      | `urn:ngsi-ld:Employee:XXX`      |

---

## Running Tests

```bash
pytest tests/
```

14 tests covering models and routes.

---

## Internationalization

The app supports 4 languages switchable from the navbar:

| Code | Language |
| ---- | -------- |
| `en` | English  |
| `es` | Español  |
| `gl` | Galego   |
| `de` | Deutsch  |

To add a new language:

```bash
pybabel init -i messages.pot -d translations -l <lang_code>
# Edit translations/<lang_code>/LC_MESSAGES/messages.po
pybabel compile -d translations
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE) © 2026 Nicolás Aller Ponte
