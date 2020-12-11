from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .controller.controller_risk import risk_blueprint

        app.register_blueprint(risk_blueprint)

    return app
