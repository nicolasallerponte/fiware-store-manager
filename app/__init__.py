from flask import Flask, request, session
from flask_babel import Babel
from .models import db
from .routes import register_blueprints
from dotenv import load_dotenv
import requests
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

def get_locale():
    # if a user is logged in, use the locale from the user settings
    return session.get('language', request.accept_languages.best_match(['en', 'es', 'gl', 'de']))

babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev' # needed for session
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smart_store.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Orion Configuration
    orion_url = os.getenv('ORION_URL', 'http://localhost:1026')
    app.config['ORION_URL'] = orion_url
    
    # Translations are in the root directory
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = '../translations'

    db.init_app(app)
    babel.init_app(app, locale_selector=get_locale)

    register_blueprints(app)

    # Orion connectivity check
    try:
        response = requests.get(f"{orion_url}/version", timeout=2)
        if response.status_code == 200:
            logger.info(f"Orion Context Broker available at {orion_url}")
            app.config['USE_ORION'] = True
        else:
            logger.warning(f"Orion returned status {response.status_code}, falling back to SQLite")
            app.config['USE_ORION'] = False
    except requests.exceptions.RequestException:
        logger.warning("Orion not available, falling back to SQLite")
        app.config['USE_ORION'] = False

    return app
