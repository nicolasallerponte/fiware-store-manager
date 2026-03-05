import os
from app import create_app
from app.models import db, Store, Product, InventoryItem

app = create_app()

with app.app_context():
    # Drop and recreate tables
    db.drop_all()
    db.create_all()

    # Create 4 Stores
    stores = [
        Store(name='Smart Store Downtown', location='123 Main St, City Center'),
        Store(name='Smart Store North', location='456 North Blvd, Uptown'),
        Store(name='Smart Store Eastside', location='789 East Ave, Eastside'),
        Store(name='Smart Store West', location='101 West Ln, Westside')
    ]
    db.session.add_all(stores)
    db.session.commit()

    # Create 10 distinct Products
    products = [
        Product(name='Organic Apples', description='Fresh organic apples from local farms.', price=2.99),
        Product(name='Whole Milk', description='1 Gallon of whole milk.', price=3.49),
        Product(name='Artisan Bread', description='Freshly baked sourdough bread.', price=4.50),
        Product(name='Free Range Eggs', description='Dozen brown eggs.', price=5.25),
        Product(name='Avocados', description='Ripe Hass avocados.', price=1.50),
        Product(name='Coffee Beans', description='Dark roast coffee beans, 1lb.', price=12.99),
        Product(name='Almond Butter', description='Creamy unsalted almond butter.', price=8.49),
        Product(name='Greek Yogurt', description='Plain greek yogurt, 32oz.', price=5.99),
        Product(name='Spinach', description='Fresh baby spinach leaves.', price=3.99),
        Product(name='Pasta', description='Italian penne pasta, 1lb.', price=2.49)
    ]
    db.session.add_all(products)
    db.session.commit()

    # Distribute products items across stores
    # Guarantee at least 5 products belong to one specific store (Store 1: Smart Store Downtown)
    inventory_items = [
        # Store 1 gets 6 products
        InventoryItem(store_id=stores[0].id, product_id=products[0].id, stock_quantity=50),
        InventoryItem(store_id=stores[0].id, product_id=products[1].id, stock_quantity=30),
        InventoryItem(store_id=stores[0].id, product_id=products[2].id, stock_quantity=20),
        InventoryItem(store_id=stores[0].id, product_id=products[3].id, stock_quantity=45),
        InventoryItem(store_id=stores[0].id, product_id=products[4].id, stock_quantity=60),
        InventoryItem(store_id=stores[0].id, product_id=products[5].id, stock_quantity=15),
        
        # Store 2 gets 3 products
        InventoryItem(store_id=stores[1].id, product_id=products[6].id, stock_quantity=25),
        InventoryItem(store_id=stores[1].id, product_id=products[7].id, stock_quantity=40),
        InventoryItem(store_id=stores[1].id, product_id=products[8].id, stock_quantity=35),

        # Store 3 gets 3 products
        InventoryItem(store_id=stores[2].id, product_id=products[9].id, stock_quantity=100),
        InventoryItem(store_id=stores[2].id, product_id=products[0].id, stock_quantity=40),
        InventoryItem(store_id=stores[2].id, product_id=products[1].id, stock_quantity=20),

        # Store 4 gets 2 products
        InventoryItem(store_id=stores[3].id, product_id=products[5].id, stock_quantity=10),
        InventoryItem(store_id=stores[3].id, product_id=products[8].id, stock_quantity=15),
    ]

    db.session.add_all(inventory_items)
    db.session.commit()
    print('Database initialized with sample data successfully.')
