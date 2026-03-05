from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def generate_urn(entity_type, number):
    """Helper to generate URN format urn:ngsi-ld:{EntityType}:{number:03d}"""
    return f"urn:ngsi-ld:{entity_type}:{number:03d}"

class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.String(100), primary_key=True)  # urn:ngsi-ld:Store:XXX
    name = db.Column(db.String(100), nullable=False)
    address_street = db.Column(db.String(200), nullable=False)
    address_locality = db.Column(db.String(100), nullable=False)
    address_region = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=True)

    # Relationships
    shelves = db.relationship('Shelf', back_populates='store', cascade='all, delete-orphan')
    inventory = db.relationship('InventoryItem', back_populates='store', cascade='all, delete-orphan')
    employees = db.relationship('Employee', back_populates='store', cascade='all, delete-orphan')

class Shelf(db.Model):
    __tablename__ = 'shelves'
    id = db.Column(db.String(100), primary_key=True)  # urn:ngsi-ld:Shelf:XXX
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    max_capacity = db.Column(db.Integer, nullable=False)
    ref_store = db.Column(db.String(100), db.ForeignKey('stores.id'), nullable=False)

    # Relationships
    store = db.relationship('Store', back_populates='shelves')
    inventory = db.relationship('InventoryItem', back_populates='shelf', cascade='all, delete-orphan')

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(100), primary_key=True)  # urn:ngsi-ld:Product:XXX
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(20), nullable=False)  # Small/Medium/Large/XL
    image = db.Column(db.String(255), nullable=True)
    origin_country = db.Column(db.String(100), nullable=False)

    # Relationships
    inventory = db.relationship('InventoryItem', back_populates='product', cascade='all, delete-orphan')

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    id = db.Column(db.String(100), primary_key=True)  # urn:ngsi-ld:InventoryItem:XXX
    ref_store = db.Column(db.String(100), db.ForeignKey('stores.id'), nullable=False)
    ref_product = db.Column(db.String(100), db.ForeignKey('products.id'), nullable=False)
    ref_shelf = db.Column(db.String(100), db.ForeignKey('shelves.id'), nullable=False)
    stock_count = db.Column(db.Integer, default=0)
    shelf_count = db.Column(db.Integer, default=0)

    # Relationships
    store = db.relationship('Store', back_populates='inventory')
    product = db.relationship('Product', back_populates='inventory')
    shelf = db.relationship('Shelf', back_populates='inventory')

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.String(100), primary_key=True)  # urn:ngsi-ld:Employee:XXX
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    salary = db.Column(db.Float, nullable=False)
    role = db.Column(db.String(100), nullable=False)
    ref_store = db.Column(db.String(100), db.ForeignKey('stores.id'), nullable=False)

    # Relationships
    store = db.relationship('Store', back_populates='employees')
