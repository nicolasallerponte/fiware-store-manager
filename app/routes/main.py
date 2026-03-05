from flask import Blueprint, render_template, session, redirect, request, current_app
from flask_babel import _
from app.models import Store, Product, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def dashboard():
    total_stores = Store.query.count()
    total_products = Product.query.count()
    use_orion = current_app.config.get('USE_ORION', False)
    return render_template('dashboard.html', total_stores=total_stores, total_products=total_products, use_orion=use_orion)

@main_bp.route('/set_locale/<locale>')
def set_locale(locale):
    if locale in ['en', 'es', 'gl', 'de']:
        session['language'] = locale
    return redirect(request.referrer or '/')
