from app import create_app
from app.models import db, Store, Shelf, Product, InventoryItem, Employee, generate_urn

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # ─── Stores (16) ──────────────────────────────────────────────────────────
    stores_data = [
        ('Smart Store A Coruña',  'Rúa Real 12',            'A Coruña',  'Galicia',       43.3713,  -8.3959, 'https://images.unsplash.com/photo-1534452203293-494d7ddbf7e0?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Madrid',    'Gran Vía 28',            'Madrid',    'Madrid',        40.4168,  -3.7038, 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Barcelona', 'Passeig de Gràcia 55',   'Barcelona', 'Cataluña',      41.3851,   2.1734, 'https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Sevilla',   'Calle Sierpes 10',       'Sevilla',   'Andalucía',     37.3886,  -5.9823, 'https://images.unsplash.com/photo-1578916171728-46686eac8d58?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Valencia',  'Av. del Puerto 4',       'Valencia',  'Valencia',      39.4699,  -0.3763, 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Lisboa',    'Rua Augusta 80',         'Lisboa',    'Lisboa',        38.7223,  -9.1393, 'https://images.unsplash.com/photo-1587467512961-120760940315?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Porto',     'Rua Santa Catarina 12',  'Porto',     'Norte',         41.1579,  -8.6291, 'https://images.unsplash.com/photo-1567521464027-f127ff144326?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Paris',     'Rue de Rivoli 100',      'París',     'Île-de-France', 48.8566,   2.3522, 'https://images.unsplash.com/photo-1441984904996-e0b6ba687e04?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Lyon',      'Rue de la République 5', 'Lyon',      'Auvergne-RA',   45.7640,   4.8357, 'https://images.unsplash.com/photo-1601924994987-69e26d50dc26?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Berlín',    'Unter den Linden 20',    'Berlín',    'Berlín',        52.5200,  13.4050, 'https://images.unsplash.com/photo-1604719312566-8912e9227c6a?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Múnich',    'Marienplatz 8',          'Múnich',    'Baviera',       48.1351,  11.5820, 'https://images.unsplash.com/photo-1528698827591-e19ccd7bc23d?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Roma',      'Via del Corso 44',       'Roma',      'Lazio',         41.9028,  12.4964, 'https://images.unsplash.com/photo-1580913428735-bd3c269d6a82?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Milán',     'Corso Buenos Aires 22',  'Milán',     'Lombardía',     45.4654,   9.1859, 'https://images.unsplash.com/photo-1472491235688-bdc81a63246e?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Ámsterdam', 'Kalverstraat 15',        'Ámsterdam', 'Noord-Holland', 52.3676,   4.9041, 'https://images.unsplash.com/photo-1620735692151-26a7e0748429?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Bruselas',  'Rue Neuve 30',           'Bruselas',  'Bruselas',      50.8503,   4.3517, 'https://images.unsplash.com/photo-1559329007-40df8a9345d8?auto=format&fit=crop&q=80&w=400'),
        ('Smart Store Viena',     'Mariahilfer Str. 60',    'Viena',     'Viena',         48.2082,  16.3738, 'https://images.unsplash.com/photo-1571867424488-4565932edb41?auto=format&fit=crop&q=80&w=400'),
    ]

    stores = []
    for i, (name, street, city, region, lat, lng, img) in enumerate(stores_data):
        stores.append(Store(
            id=generate_urn('Store', i+1),
            name=name,
            address_street=street,
            address_locality=city,
            address_region=region,
            latitude=lat,
            longitude=lng,
            image=img
        ))
    db.session.add_all(stores)

    # ─── Shelves (2 per store) ─────────────────────────────────────────────────
    shelves = []
    for i, store in enumerate(stores):
        for j in range(2):
            shelves.append(Shelf(
                id=generate_urn('Shelf', i*2 + j + 1),
                name=f'Estantería {j+1}',
                latitude=store.latitude,
                longitude=store.longitude,
                max_capacity=120,
                ref_store=store.id
            ))
    db.session.add_all(shelves)
    db.session.commit()

    # ─── Products (40) ────────────────────────────────────────────────────────
    # Renames: Jamón Serrano→Filete Ternera, Almendras→Chucherías,
    #          Atún en Conserva→Ensalada, Mermelada de Fresa→Batido,
    #          Leche de Avena→Smoothie
    # Images kept identical to previous version on all renamed products.
    products_data = [
        ('Manzanas Ecológicas',      2.99, 'medium', 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&q=80&w=200',  'España'),
        ('Leche Entera',             3.49, 'large',  'https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&q=80&w=200',  'Dinamarca'),
        ('Pan Artesano',             4.50, 'large',  'https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&q=80&w=200', 'Francia'),
        ('Huevos de Corral',         5.25, 'medium', 'https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&q=80&w=200', 'Países Bajos'),
        ('Aguacates',                1.50, 'small',  'https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?auto=format&fit=crop&q=80&w=200', 'México'),
        ('Café en Grano',           12.99, 'medium', 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&q=80&w=200',  'Colombia'),
        ('Mantequilla de Almendras', 8.49, 'small',  'https://images.unsplash.com/photo-1590301157890-4810ed352733?auto=format&fit=crop&q=80&w=200', 'España'),
        ('Yogur Griego',             5.99, 'large',  'https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&q=80&w=200', 'Grecia'),
        ('Espinacas',                3.99, 'medium', 'https://images.unsplash.com/photo-1576045057995-568f588f82fb?auto=format&fit=crop&q=80&w=200', 'Italia'),
        ('Pasta',                    2.49, 'medium', 'https://images.unsplash.com/photo-1551462147-ff29053bfc14?auto=format&fit=crop&q=80&w=200',  'Italia'),
        ('Tomates Cherry',           3.20, 'small',  'https://images.unsplash.com/photo-1592841200221-a6898f307baa?auto=format&fit=crop&q=80&w=200', 'España'),
        ('Queso Manchego',           9.80, 'medium', 'https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?auto=format&fit=crop&q=80&w=200', 'España'),
        ('Aceite de Oliva',          7.50, 'large',  'https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&q=80&w=200', 'España'),
        ('Salmón Ahumado',          11.99, 'medium', 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&q=80&w=200', 'Noruega'),
        ('Arroz Integral',           2.80, 'large',  'https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&q=80&w=200', 'Italia'),
        ('Garbanzos',                2.10, 'medium', 'https://images.unsplash.com/photo-1515543904379-3d757afe72e4?auto=format&fit=crop&q=80&w=200', 'España'),
        ('Chocolate Negro',          4.25, 'small',  'https://images.unsplash.com/photo-1481391319762-47dff72954d9?auto=format&fit=crop&q=80&w=200', 'Bélgica'),
        ('Miel de Abeja',            6.90, 'small',  'https://images.unsplash.com/photo-1558642452-9d2a7deb7f62?auto=format&fit=crop&q=80&w=200',  'España'),
        ('Zumo de Naranja',          3.60, 'large',  'https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&q=80&w=200', 'España'),
        ('Cerveza Artesana',         2.99, 'medium', 'https://images.unsplash.com/photo-1535958636474-b021ee887b13?auto=format&fit=crop&q=80&w=200', 'Alemania'),
        ('Vino Tinto',              10.50, 'large',  'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?auto=format&fit=crop&q=80&w=200', 'España'),
        ('Filete Ternera',          18.00, 'large',  'https://images.unsplash.com/photo-1600891964092-4316c288032e?auto=format&fit=crop&q=80&w=200',  'España'),
        ('Patatas',                  1.80, 'large',  'https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&q=80&w=200', 'Países Bajos'),
        ('Cebollas',                 1.20, 'medium', 'https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?auto=format&fit=crop&q=80&w=200', 'España'),
        ('Zanahorias',               1.50, 'medium', 'https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&fit=crop&q=80&w=200', 'Francia'),
        ('Brócoli',                  2.40, 'medium', 'https://images.unsplash.com/photo-1584270354949-c26b0d5b4a0c?auto=format&fit=crop&q=80&w=200', 'Italia'),
        ('Plátanos',                 1.90, 'large',  'https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&q=80&w=200', 'Colombia'),
        ('Naranjas',                 2.50, 'large',  'https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&fit=crop&q=80&w=200',  'España'),
        ('Fresas',                   3.80, 'small',  'https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&q=80&w=200', 'España'),
        ('Arándanos',                4.50, 'small',  'https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&q=80&w=200', 'Polonia'),
        ('Nueces',                   5.60, 'small',  'https://images.unsplash.com/photo-1606923829579-0cb981a83e2e?auto=format&fit=crop&q=80&w=200',  'Francia'),
        ('Chucherías',               6.20, 'small',  'https://images.unsplash.com/photo-1621939514649-280e2ee25f60?auto=format&fit=crop&q=80&w=200',  'España'),
        ('Ensalada',                 3.10, 'small',  'https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?auto=format&fit=crop&q=80&w=200',  'Portugal'),
        ('Sardinas en Aceite',       2.80, 'small',  'https://images.unsplash.com/photo-1534482421-64566f976cfa?auto=format&fit=crop&q=80&w=200',  'Portugal'),
        ('Batido',                   3.40, 'small',  'https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&q=80&w=200',  'Francia'),
        ('Té Verde',                 5.80, 'small',  'https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&q=80&w=200',  'Japón'),
        ('Harina de Trigo',          1.60, 'large',  'https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?auto=format&fit=crop&q=80&w=200', 'Francia'),
        ('Mantequilla',              3.20, 'medium', 'https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&q=80&w=200', 'Francia'),
        ('Smoothie',                 2.90, 'large',  'https://images.unsplash.com/photo-1603569283847-aa295f0d016a?auto=format&fit=crop&q=80&w=200',  'Suecia'),
        ('Hummus',                   3.70, 'medium', 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&q=80&w=200', 'Líbano'),
    ]

    products = []
    for i, (name, price, size, img, origin) in enumerate(products_data):
        products.append(Product(
            id=generate_urn('Product', i+1),
            name=name,
            price=price,
            size=size,
            image=img,
            origin_country=origin
        ))
    db.session.add_all(products)
    db.session.commit()

    # ─── Inventory (5 products per store, varied) ─────────────────────────────
    inventory_items = []
    inv_counter = 1
    for s_idx, store in enumerate(stores):
        shelf_a = shelves[s_idx * 2]
        shelf_b = shelves[s_idx * 2 + 1]
        for p_offset in range(5):
            p_idx = (s_idx * 3 + p_offset) % len(products)
            shelf = shelf_a if p_offset < 3 else shelf_b
            inventory_items.append(InventoryItem(
                id=generate_urn('InventoryItem', inv_counter),
                ref_store=store.id,
                ref_product=products[p_idx].id,
                ref_shelf=shelf.id,
                stock_count=20 + (p_offset * 7),
                shelf_count=5 + p_offset
            ))
            inv_counter += 1
    db.session.add_all(inventory_items)

    # ─── Employees (32, 2 per store) ──────────────────────────────────────────
    employees_data = [
        ('Nicolás Aller',     'Store Manager',        45000, 'https://images.unsplash.com/photo-1531384441138-2736e62e0919?auto=format&fit=crop&q=80&w=400', 0),
        ('Jacobo Cousillas',  'Sales Associate',      32000, 'https://images.unsplash.com/photo-1552058544-f2b08422138a?auto=format&fit=crop&q=80&w=400', 0),
        ('Carlos Ruiz',       'Store Manager',        47000, 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&q=80&w=400', 1),
        ('Laura Martínez',    'Cashier',              28000, 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&q=80&w=400', 1),
        ('Marc Puig',         'Store Manager',        46000, 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&q=80&w=400', 2),
        ('Laia Ferrer',       'Inventory Specialist', 35000, 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=400', 2),
        ('Pedro Morales',     'Store Manager',        44000, 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&q=80&w=400', 3),
        ('Carmen Vega',       'Sales Associate',      31000, 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&q=80&w=400', 3),
        ('Jordi Soler',       'Store Manager',        45500, 'https://images.unsplash.com/photo-1463453091185-61582044d556?auto=format&fit=crop&q=80&w=400', 4),
        ('Marta Gil',         'Cashier',              27500, 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=400', 4),
        ('João Costa',        'Store Manager',        46500, 'https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&q=80&w=400', 5),
        ('Ana Rodrigues',     'Sales Associate',      30000, 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?auto=format&fit=crop&q=80&w=400', 5),
        ('Rui Oliveira',      'Store Manager',        44500, 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&q=80&w=400', 6),
        ('Sofia Pereira',     'Inventory Specialist', 34000, 'https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?auto=format&fit=crop&q=80&w=400', 6),
        ('Élodie Dupont',     'Store Manager',        52000, 'https://images.unsplash.com/photo-1554151228-14d9def656e4?auto=format&fit=crop&q=80&w=400', 7),
        ('Lucas Martin',      'Sales Associate',      36000, 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?auto=format&fit=crop&q=80&w=400', 7),
        ('Camille Bernard',   'Store Manager',        49000, 'https://images.unsplash.com/photo-1502685104226-ee32379fefbe?auto=format&fit=crop&q=80&w=400', 8),
        ('Antoine Petit',     'Cashier',              32000, 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?auto=format&fit=crop&q=80&w=400', 8),
        ('Klaus Müller',      'Store Manager',        53000, 'https://images.unsplash.com/photo-1566492031773-4f4e44671857?auto=format&fit=crop&q=80&w=400', 9),
        ('Lena Schmidt',      'Inventory Specialist', 38000, 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=400', 9),
        ('Hans Wagner',       'Store Manager',        54000, 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&q=80&w=400', 10),
        ('Emma Fischer',      'Sales Associate',      35000, 'https://images.unsplash.com/photo-1589571894960-20bbe2828d0a?auto=format&fit=crop&q=80&w=400', 10),
        ('Marco Esposito',    'Store Manager',        48000, 'https://images.unsplash.com/photo-1504257432389-52343af06ae3?auto=format&fit=crop&q=80&w=400', 11),
        ('Giulia Romano',     'Cashier',              29000, 'https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?auto=format&fit=crop&q=80&w=400', 11),
        ('Lorenzo Ricci',     'Store Manager',        51000, 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&q=80&w=400', 12),
        ('Francesca Marino',  'Inventory Specialist', 36000, 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&q=80&w=400', 12),
        ('Daan de Vries',     'Store Manager',        55000, 'https://images.unsplash.com/photo-1480429370139-e0132c086e2a?auto=format&fit=crop&q=80&w=400', 13),
        ('Sophie van Berg',   'Sales Associate',      37000, 'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?auto=format&fit=crop&q=80&w=400', 13),
        ('Thomas Leroy',      'Store Manager',        50000, 'https://images.unsplash.com/photo-1519345182560-3f2917c472ef?auto=format&fit=crop&q=80&w=400', 14),
        ('Nathalie Simon',    'Cashier',              33000, 'https://images.unsplash.com/photo-1499952127939-9bbf5af6c51c?auto=format&fit=crop&q=80&w=400', 14),
        ('Wolfgang Huber',    'Store Manager',        53500, 'https://images.unsplash.com/photo-1540569014015-19a7be504e3a?auto=format&fit=crop&q=80&w=400', 15),
        ('Katharina Bauer',   'Sales Associate',      34500, 'https://images.unsplash.com/photo-1523824921871-d6f1a15151f1?auto=format&fit=crop&q=80&w=400', 15),
    ]

    employees = []
    for i, (name, role, salary, img, store_idx) in enumerate(employees_data):
        employees.append(Employee(
            id=generate_urn('Employee', i+1),
            name=name,
            role=role,
            salary=float(salary),
            image=img,
            ref_store=stores[store_idx].id
        ))
    db.session.add_all(employees)
    db.session.commit()
    print('Database initialized: 16 stores · 40 products · 32 employees.')