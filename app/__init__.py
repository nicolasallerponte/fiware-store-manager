from flask import Flask, request, session
from flask_babel import Babel
from .models import db
from .routes import register_blueprints
import os

def get_locale():
    # if a user is logged in, use the locale from the user settings
    return session.get('language', request.accept_languages.best_match(['en', 'es', 'gl', 'de']))

babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev' # needed for session
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smart_store.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Translations are in the root directory
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = '../translations'

    db.init_app(app)
    babel.init_app(app, locale_selector=get_locale)

    register_blueprints(app)

    return app
