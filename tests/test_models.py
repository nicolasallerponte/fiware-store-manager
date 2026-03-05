import pytest
from app.models import Store, Product, Shelf, InventoryItem, generate_urn

def test_store_persistence(db_session):
    """Test creating a Store and verify it persists."""
    store_id = generate_urn('Store', 101)
    store = Store(
        id=store_id,
        name="Persistence Store",
        address_street="123 Alpha St",
        address_locality="Locality",
        address_region="Region",
        latitude=1.0,
        longitude=1.0
    )
    db_session.add(store)
    db_session.commit()

    saved_store = db_session.get(Store, store_id)
    assert saved_store is not None
    assert saved_store.name == "Persistence Store"
    assert saved_store.address_street == "123 Alpha St"

def test_product_persistence(db_session):
    """Test creating a Product and verify it persists."""
    product_id = generate_urn('Product', 101)
    product = Product(
        id=product_id,
        name="Persistence Product",
        price=19.99,
        size="Medium",
        origin_country="Spain"
    )
    db_session.add(product)
    db_session.commit()

    saved_product = db_session.get(Product, product_id)
    assert saved_product is not None
    assert saved_product.name == "Persistence Product"
    assert saved_product.price == 19.99

def test_shelf_persistence(db_session):
    """Test creating a Shelf and verify it persists."""
    store = Store(id=generate_urn('Store', 102), name="S2", address_street="S", address_locality="L", address_region="R", latitude=0, longitude=0)
    db_session.add(store)
    db_session.commit()

    shelf_id = generate_urn('Shelf', 101)
    shelf = Shelf(id=shelf_id, name="Shelf 1", latitude=0, longitude=0, max_capacity=50, ref_store=store.id)
    db_session.add(shelf)
    db_session.commit()

    saved_shelf = db_session.get(Shelf, shelf_id)
    assert saved_shelf is not None
    assert saved_shelf.name == "Shelf 1"
    assert saved_shelf.ref_store == store.id

def test_inventory_item_relationship(db_session):
    """Test creating an InventoryItem linking Store, Product and Shelf."""
    store = Store(id=generate_urn('Store', 103), name="S3", address_street="S", address_locality="L", address_region="R", latitude=0, longitude=0)
    product = Product(id=generate_urn('Product', 103), name="P3", price=5.0, size="S", origin_country="C")
    db_session.add_all([store, product])
    db_session.commit()
    
    shelf = Shelf(id=generate_urn('Shelf', 103), name="SH3", latitude=0, longitude=0, max_capacity=10, ref_store=store.id)
    db_session.add(shelf)
    db_session.commit()

    ii_id = generate_urn('InventoryItem', 103)
    item = InventoryItem(id=ii_id, store=store, product=product, shelf=shelf, stock_count=100, shelf_count=10)
    db_session.add(item)
    db_session.commit()

    saved_item = db_session.get(InventoryItem, ii_id)
    assert saved_item is not None
    assert saved_item.stock_count == 100
    assert saved_item.store.name == "S3"
    assert saved_item.product.name == "P3"
    assert saved_item.shelf.name == "SH3"

def test_store_cascade_delete(db_session):
    """Test deleting a Store and verify cascade deletes its Shelves and InventoryItems."""
    store = Store(id=generate_urn('Store', 104), name="S4", address_street="S", address_locality="L", address_region="R", latitude=0, longitude=0)
    product = Product(id=generate_urn('Product', 104), name="P4", price=1.0, size="S", origin_country="C")
    db_session.add_all([store, product])
    db_session.commit()

    shelf = Shelf(id=generate_urn('Shelf', 104), name="SH4", latitude=0, longitude=0, max_capacity=10, ref_store=store.id)
    db_session.add(shelf)
    db_session.commit()

    ii_id = generate_urn('InventoryItem', 104)
    item = InventoryItem(id=ii_id, store=store, product=product, shelf=shelf, stock_count=10)
    db_session.add(item)
    db_session.commit()

    # Verify exists
    assert db_session.query(InventoryItem).filter_by(ref_store=store.id).count() == 1
    assert db_session.query(Shelf).filter_by(ref_store=store.id).count() == 1

    # Delete store
    db_session.delete(store)
    db_session.commit()

    # Verify item and shelf are gone
    assert db_session.query(InventoryItem).filter_by(ref_store=store.id).count() == 0
    assert db_session.query(Shelf).filter_by(ref_store=store.id).count() == 0
    # Verify product still exists
    assert db_session.get(Product, product.id) is not None
