from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Store, Product, InventoryItem, generate_urn
from flask_babel import _

products_bp = Blueprint('products', __name__)

@products_bp.route('/')
def index():
    products = Product.query.all()
    return render_template('products/index.html', products=products)

@products_bp.route('/<string:product_id>')
def detail(product_id):
    product = Product.query.get_or_404(product_id)
    all_stores = Store.query.all()
    return render_template('products/detail.html', product=product, all_stores=all_stores)

@products_bp.route('/<string:product_id>/inventory/add', methods=['POST'])
def add_inventory(product_id):
    store_id = request.form.get('store_id')
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
    flash(_('Product added to store inventory successfully.'))
    return redirect(url_for('products.detail', product_id=product_id))

@products_bp.route('/<string:product_id>/inventory/<string:item_id>/edit', methods=['POST'])
def edit_inventory(product_id, item_id):
    item = InventoryItem.query.get_or_404(item_id)
    item.stock_count = int(request.form.get('stock_count', item.stock_count))
    item.shelf_count = int(request.form.get('shelf_count', item.shelf_count))
    item.ref_shelf = request.form.get('ref_shelf', item.ref_shelf)
    
    db.session.commit()
    flash(_('Inventory item updated successfully.'))
    return redirect(url_for('products.detail', product_id=product_id))

@products_bp.route('/<string:product_id>/inventory/<string:item_id>/delete', methods=['POST'])
def delete_inventory(product_id, item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash(_('Inventory item deleted successfully.'))
    return redirect(url_for('products.detail', product_id=product_id))
