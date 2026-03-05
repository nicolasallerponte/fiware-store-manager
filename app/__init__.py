from flask import Flask
from .models import db
from .routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smart_store.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    register_blueprints(app)

    return app
