from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "student-task-manager-secret"

    from app.routes import main
    app.register_blueprint(main)

    return app
# Flask application initialization
