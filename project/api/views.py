from flask import Blueprint

from database_singleton import Singleton
from project.api.utils.creation_utils import Utils

example_blueprint = Blueprint("example", __name__)
db = Singleton().database_connection()
utils = Utils()


@example_blueprint.get("/ping")
def pong():
    return {"message": "works!"}, 200
