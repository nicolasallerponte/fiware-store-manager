# Contributing to fiware-smart-store

Thank you for your interest in contributing! This document outlines the process for contributing to this project.

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## How to Contribute

### Reporting Bugs

Before opening a bug report, please check if an issue already exists. If not, open a new issue with:

- A clear, descriptive title
- Steps to reproduce the problem
- Expected vs actual behavior
- Your environment (OS, Python version, Docker version)
- Relevant logs or screenshots

### Suggesting Features

Open an issue with the `enhancement` label. Describe the feature, the problem it solves, and any implementation ideas you have.

### Submitting a Pull Request

1. **Fork** the repository
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```
3. **Make your changes** following the code style below
4. **Add or update tests** if applicable
5. **Run the test suite** and ensure all tests pass:
   ```bash
   pytest tests/
   ```
6. **Commit** using [Conventional Commits](https://www.conventionalcommits.org/):
   ```
   feat: add new entity type
   fix: correct inventory deletion bug
   docs: update architecture diagram
   chore: bump dependencies
   ```
7. **Push** your branch and open a Pull Request against `main`

---

## Development Setup

```bash
git clone https://github.com/nicolasallerponte/fiware-store-manager.git
cd fiware-store-manager
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python init_db.py
python run.py
```

---

## Code Style

- Follow **PEP 8** for Python code
- Use **type hints** where practical
- Keep routes in their respective Blueprint files under `app/routes/`
- All new UI strings must be wrapped in `_()` for i18n
- New entities must follow the FIWARE NGSIv2 URN pattern: `urn:ngsi-ld:EntityType:XXX`
- Use `generate_urn(entity_type, number)` from `models.py` for new entity IDs

---

## Running Tests

```bash
pytest tests/
```

Please add tests for any new routes or models you introduce. Test files live in `tests/`.

---

## Translations

If you add new UI strings, update the translation catalogs:

```bash
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d translations
# Edit .po files for each language
pybabel compile -d translations
```

---

## Questions

Feel free to open an issue with the `question` label if you need help.
