class RouteApp:
    def init_app(self, app):
        from app.resources import box_bp, product_history_bp
        app.register_blueprint(product_history_bp, url_prefix='/api/v1')
        app.register_blueprint(box_bp, url_prefix='/api/v1')


