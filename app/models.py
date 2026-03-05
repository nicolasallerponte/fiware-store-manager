from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    inventory = db.relationship('InventoryItem', back_populates='store', cascade='all, delete-orphan')

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    inventory = db.relationship('InventoryItem', back_populates='product', cascade='all, delete-orphan')

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    stock_quantity = db.Column(db.Integer, default=0)

    # Relationships
    store = db.relationship('Store', back_populates='inventory')
    product = db.relationship('Product', back_populates='inventory')
