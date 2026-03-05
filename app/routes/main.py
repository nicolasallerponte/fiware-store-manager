from flask import Blueprint, render_template, session, redirect, request
from flask_babel import _
from app.models import Store, Product, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def dashboard():
    total_stores = Store.query.count()
    total_products = Product.query.count()
    return render_template('dashboard.html', total_stores=total_stores, total_products=total_products)

@main_bp.route('/set_locale/<locale>')
def set_locale(locale):
    if locale in ['en', 'es', 'gl', 'de']:
        session['language'] = locale
    return redirect(request.referrer or '/')
