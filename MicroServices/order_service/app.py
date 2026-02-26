from flask import Flask
from services.order import order_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(order_bp)

    @app.route('/')
    def index():
        return "Order microservice"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5003, debug=True)