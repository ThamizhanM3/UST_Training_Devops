from flask import Flask
from services.product import product_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(product_bp)

    @app.route('/')
    def index():
        return "Product microservice"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5002, debug=True)