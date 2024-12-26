import os

from flask import Flask
from flask_migrate import Migrate

from project.api.models import db
from project.api.views import example_blueprint

migrate = Migrate()


# instantiate the app
def create_app(script_info=None):
    # Instantiate the app
    app = Flask(__name__)

    # Set Configuration
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # Set up Database
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    # register blueprints
    app.register_blueprint(example_blueprint, url_prefix="/example")

    # shell context for flask cli
    @app.shell_context_processor
    def shell_context():
        return {"app": app, "db": db}

    return app
