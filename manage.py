from project import create_app
from flask.cli import FlaskGroup
from flask import current_app

# Config coverage report
app = create_app()
cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()
