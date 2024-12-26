from flask import Blueprint

example_blueprint = Blueprint("example", __name__)


@example_blueprint.get("/ping")
def pong():
    return {"message": "works!"}, 200
