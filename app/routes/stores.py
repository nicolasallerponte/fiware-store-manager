from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Store, Shelf, Product, InventoryItem, generate_urn
from flask_babel import _

stores_bp = Blueprint('stores', __name__)

@stores_bp.route('/')
def index():
    stores = Store.query.all()
    return render_template('stores/index.html', stores=stores)

@stores_bp.route('/<string:store_id>')
def detail(store_id):
    store = Store.query.get_or_404(store_id)
    all_products = Product.query.all()
    return render_template('stores/detail.html', store=store, all_products=all_products)

@stores_bp.route('/<string:store_id>/inventory/add', methods=['POST'])
def add_inventory(store_id):
    product_id = request.form.get('product_id')
    stock_count = int(request.form.get('stock_count', 0))
    shelf_count = int(request.form.get('shelf_count', 0))
    ref_shelf = request.form.get('ref_shelf')
    
    # Simple ID generation based on count
    count = InventoryItem.query.count()
    item_id = generate_urn('InventoryItem', count + 1)
    
    new_item = InventoryItem(
        id=item_id,
        ref_store=store_id,
        ref_product=product_id,
        ref_shelf=ref_shelf,
        stock_count=stock_count,
        shelf_count=shelf_count
    )
    db.session.add(new_item)
    db.session.commit()
    flash(_('Product added to inventory successfully.'))
    return redirect(url_for('stores.detail', store_id=store_id))

@stores_bp.route('/<string:store_id>/inventory/<string:item_id>/edit', methods=['POST'])
def edit_inventory(store_id, item_id):
    item = InventoryItem.query.get_or_404(item_id)
    item.stock_count = int(request.form.get('stock_count', item.stock_count))
    item.shelf_count = int(request.form.get('shelf_count', item.shelf_count))
    item.ref_shelf = request.form.get('ref_shelf', item.ref_shelf)
    
    db.session.commit()
    flash(_('Inventory item updated successfully.'))
    return redirect(url_for('stores.detail', store_id=store_id))

@stores_bp.route('/<string:store_id>/inventory/<string:item_id>/delete', methods=['POST'])
def delete_inventory(store_id, item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash(_('Inventory item deleted successfully.'))
    return redirect(url_for('stores.detail', store_id=store_id))

@stores_bp.route('/<string:store_id>/shelves/add', methods=['POST'])
def add_shelf(store_id):
    name = request.form.get('name')
    max_capacity = int(request.form.get('max_capacity', 100))
    lat = float(request.form.get('latitude', 0.0))
    lng = float(request.form.get('longitude', 0.0))
    
    count = Shelf.query.count()
    shelf_id = generate_urn('Shelf', count + 1)
    
    new_shelf = Shelf(
        id=shelf_id,
        name=name,
        max_capacity=max_capacity,
        latitude=lat,
        longitude=lng,
        ref_store=store_id
    )
    db.session.add(new_shelf)
    db.session.commit()
    flash(_('Shelf added successfully.'))
    return redirect(url_for('stores.detail', store_id=store_id))

@stores_bp.route('/<string:store_id>/shelves/<string:shelf_id>/edit', methods=['POST'])
def edit_shelf(store_id, shelf_id):
    shelf = Shelf.query.get_or_404(shelf_id)
    shelf.name = request.form.get('name', shelf.name)
    shelf.max_capacity = int(request.form.get('max_capacity', shelf.max_capacity))
    shelf.latitude = float(request.form.get('latitude', shelf.latitude))
    shelf.longitude = float(request.form.get('longitude', shelf.longitude))
    
    db.session.commit()
    flash(_('Shelf updated successfully.'))
    return redirect(url_for('stores.detail', store_id=store_id))

@stores_bp.route('/<string:store_id>/shelves/<string:shelf_id>/delete', methods=['POST'])
def delete_shelf(store_id, shelf_id):
    shelf = Shelf.query.get_or_404(shelf_id)
    db.session.delete(shelf)
    db.session.commit()
    flash(_('Shelf deleted successfully.'))
    return redirect(url_for('stores.detail', store_id=store_id))
