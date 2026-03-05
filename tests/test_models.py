import pytest
from app.models import Store, Product, InventoryItem

def test_store_persistence(db_session):
    """Test creating a Store and verify it persists."""
    store = Store(name="Persistence Store", location="Location A")
    db_session.add(store)
    db_session.commit()

    saved_store = db_session.get(Store, store.id)
    assert saved_store is not None
    assert saved_store.name == "Persistence Store"
    assert saved_store.location == "Location A"

def test_product_persistence(db_session):
    """Test creating a Product and verify it persists."""
    product = Product(name="Persistence Product", price=19.99, description="Test Desc")
    db_session.add(product)
    db_session.commit()

    saved_product = db_session.get(Product, product.id)
    assert saved_product is not None
    assert saved_product.name == "Persistence Product"
    assert saved_product.price == 19.99

def test_inventory_item_relationship(db_session):
    """Test creating an InventoryItem linking Store and Product."""
    store = Store(name="Inventory Store", location="Location B")
    product = Product(name="Inventory Product", price=5.0)
    db_session.add_all([store, product])
    db_session.commit()

    item = InventoryItem(store=store, product=product, stock_quantity=100)
    db_session.add(item)
    db_session.commit()

    saved_item = db_session.query(InventoryItem).filter_by(store_id=store.id, product_id=product.id).first()
    assert saved_item is not None
    assert saved_item.stock_quantity == 100
    assert saved_item.store.name == "Inventory Store"
    assert saved_item.product.name == "Inventory Product"

def test_store_cascade_delete(db_session):
    """Test deleting a Store and verify cascade deletes its InventoryItems."""
    store = Store(name="Cascade Store", location="Location C")
    product = Product(name="Cascade Product", price=1.0)
    db_session.add_all([store, product])
    db_session.commit()

    item = InventoryItem(store=store, product=product, stock_quantity=10)
    db_session.add(item)
    db_session.commit()

    # Verify item exists
    assert db_session.query(InventoryItem).filter_by(store_id=store.id).count() == 1

    # Delete store
    db_session.delete(store)
    db_session.commit()

    # Verify item is gone
    assert db_session.query(InventoryItem).filter_by(store_id=store.id).count() == 0
    # Verify product still exists
    assert db_session.get(Product, product.id) is not None
