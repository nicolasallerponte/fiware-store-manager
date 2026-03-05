import pytest
from app.models import Store, Product, generate_urn

def test_dashboard_route(client):
    """Test that the dashboard returns 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_stores_list_route(client):
    """Test that the stores list returns 200."""
    response = client.get('/stores/')
    assert response.status_code == 200

def test_store_detail_route(client, db_session):
    """Test store detail returns 200 for existing, 404 for non-existing."""
    # Test 404
    response = client.get('/stores/urn:ngsi-ld:Store:999')
    assert response.status_code == 404

    # Create a store
    store_id = generate_urn('Store', 201)
    store = Store(
        id=store_id,
        name="Test Store",
        address_street="Test St",
        address_locality="Loc",
        address_region="Reg",
        latitude=0,
        longitude=0
    )
    db_session.add(store)
    db_session.commit()

    # Test 200
    response = client.get(f'/stores/{store_id}')
    assert response.status_code == 200
    assert b"Test Store" in response.data

def test_products_list_route(client):
    """Test that the products list returns 200."""
    response = client.get('/products/')
    assert response.status_code == 200

def test_product_detail_route(client, db_session):
    """Test product detail returns 200 for existing, 404 for non-existing."""
    # Test 404
    response = client.get('/products/urn:ngsi-ld:Product:999')
    assert response.status_code == 404

    # Create a product
    product_id = generate_urn('Product', 201)
    product = Product(id=product_id, name="Test Product", price=10.0, size="M", origin_country="US")
    db_session.add(product)
    db_session.commit()

    # Test 200
    response = client.get(f'/products/{product_id}')
    assert response.status_code == 200
    assert b"Test Product" in response.data
