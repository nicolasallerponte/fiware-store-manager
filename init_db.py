import os
from app import create_app
from app.models import db, Store, Shelf, Product, InventoryItem, generate_urn

app = create_app()

with app.app_context():
    # Drop and recreate tables
    db.drop_all()
    db.create_all()

    # Create 4 Stores
    stores = [
        Store(
            id=generate_urn('Store', 1),
            name='Smart Store Downtown',
            address_street='123 Main St',
            address_locality='New York',
            address_region='NY',
            latitude=40.7128,
            longitude=-74.0060,
            image='https://images.unsplash.com/photo-1534452203293-494d7ddbf7e0?auto=format&fit=crop&q=80&w=400'
        ),
        Store(
            id=generate_urn('Store', 2),
            name='Smart Store North',
            address_street='456 North Blvd',
            address_locality='Chicago',
            address_region='IL',
            latitude=41.8781,
            longitude=-87.6298,
            image='https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&q=80&w=400'
        ),
        Store(
            id=generate_urn('Store', 3),
            name='Smart Store Eastside',
            address_street='789 East Ave',
            address_locality='Miami',
            address_region='FL',
            latitude=25.7617,
            longitude=-80.1918,
            image='https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&q=80&w=400'
        ),
        Store(
            id=generate_urn('Store', 4),
            name='Smart Store West',
            address_street='101 West Ln',
            address_locality='San Francisco',
            address_region='CA',
            latitude=37.7749,
            longitude=-122.4194,
            image='https://images.unsplash.com/photo-1578916171728-46686eac8d58?auto=format&fit=crop&q=80&w=400'
        )
    ]
    db.session.add_all(stores)

    # Create 4 Shelves (one per store)
    shelves = [
        Shelf(
            id=generate_urn('Shelf', i+1),
            name=f'Shelf {i+1} A',
            latitude=stores[i].latitude,
            longitude=stores[i].longitude,
            max_capacity=100,
            ref_store=stores[i].id
        ) for i in range(4)
    ]
    db.session.add_all(shelves)
    db.session.commit()

    # Create 10 distinct Products
    products_data = [
        ('Organic Apples', 2.99, 'Medium', 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&q=80&w=200', 'USA'),
        ('Whole Milk', 3.49, 'Large', 'https://images.unsplash.com/photo-1563636619-e910ef2a844b?auto=format&fit=crop&q=80&w=200', 'Denmark'),
        ('Artisan Bread', 4.50, 'Large', 'https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&q=80&w=200', 'France'),
        ('Free Range Eggs', 5.25, 'Medium', 'https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&q=80&w=200', 'Netherlands'),
        ('Avocados', 1.50, 'Small', 'https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?auto=format&fit=crop&q=80&w=200', 'Mexico'),
        ('Coffee Beans', 12.99, 'Medium', 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&q=80&w=200', 'Colombia'),
        ('Almond Butter', 8.49, 'Small', 'https://images.unsplash.com/photo-1590301157890-4810ed352733?auto=format&fit=crop&q=80&w=200', 'Spain'),
        ('Greek Yogurt', 5.99, 'Large', 'https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&q=80&w=200', 'Greece'),
        ('Spinach', 3.99, 'Medium', 'https://images.unsplash.com/photo-1576045057995-568f588f82fb?auto=format&fit=crop&q=80&w=200', 'Italy'),
        ('Pasta', 2.49, 'Medium', 'https://images.unsplash.com/photo-1551462147-37885abb3e91?auto=format&fit=crop&q=80&w=200', 'Italy')
    ]
    
    products = []
    for i, (name, price, size, img, origin) in enumerate(products_data):
        p = Product(
            id=generate_urn('Product', i+1),
            name=name,
            price=price,
            size=size,
            image=img,
            origin_country=origin
        )
        products.append(p)
    db.session.add_all(products)
    db.session.commit()

    # Create InventoryItems
    # Store 1 gets 6 products
    inventory_items = []
    for i in range(6):
        inventory_items.append(InventoryItem(
            id=generate_urn('InventoryItem', i+1),
            ref_store=stores[0].id,
            ref_product=products[i].id,
            ref_shelf=shelves[0].id,
            stock_count=50,
            shelf_count=10
        ))
    
    # Other stores get some products
    for s_idx in range(1, 4):
        for p_idx in range(3):
            inventory_items.append(InventoryItem(
                id=generate_urn('InventoryItem', len(inventory_items) + 1),
                ref_store=stores[s_idx].id,
                ref_product=products[p_idx + s_idx].id,
                ref_shelf=shelves[s_idx].id,
                stock_count=30,
                shelf_count=5
            ))

    db.session.add_all(inventory_items)
    db.session.commit()
    print('Database initialized with sample data successfully.')
