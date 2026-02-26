from flask import Flask
from services.user import user_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)

    @app.route('/')
    def index():
        return "User microservice"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5001, debug=True)