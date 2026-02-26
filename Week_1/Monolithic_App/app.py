from flask import Flask

# import blueprints from services
from services.user import user_bp
from services.product import product_bp
from services.order import order_bp


def create_app():
    app = Flask(__name__)

    # register service blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    

    @app.route('/')
    def index():
        return "Monolithic Flask App with 3 services"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)