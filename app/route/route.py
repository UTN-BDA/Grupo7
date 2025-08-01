class RouteApp:
    def init_app(self, app):
        from app.resources import box_bp, product_history_bp, product_bp, user_bp, user_resource
        app.register_blueprint(product_history_bp, url_prefix='/api/v1')
        app.register_blueprint(box_bp, url_prefix='/api/v1')
        app.register_blueprint(product_bp, url_prefix='/api/v1')
        app.register_blueprint(user_bp, url_prefix='/api/v1')
