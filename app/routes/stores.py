from flask import Blueprint, render_template
from app.models import Store, InventoryItem

stores_bp = Blueprint('stores', __name__)

@stores_bp.route('/')
def index():
    stores = Store.query.all()
    return render_template('stores/index.html', stores=stores)

@stores_bp.route('/<string:store_id>')
def detail(store_id):
    store = Store.query.get_or_404(store_id)
    return render_template('stores/detail.html', store=store)
