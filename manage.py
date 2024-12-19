from flask.cli import FlaskGroup

from project import create_app

# FlaskGroup is a class that is used to create a command line interface for the Flask application.
cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
