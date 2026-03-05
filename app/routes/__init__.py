def register_blueprints(app):
    from .main import main_bp
    from .stores import stores_bp
    from .products import products_bp
    from .employees import employees_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(stores_bp, url_prefix='/stores')
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(employees_bp)
