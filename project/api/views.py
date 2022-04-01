from flask import Blueprint, jsonify

from database_singleton import Singleton
from project.api.utils.creation_utils import Utils

example_blueprint = Blueprint("example", __name__)
db = Singleton().database_connection()
utils = Utils()


@example_blueprint.route("/ping", methods=["GET"])
def pong():
    return jsonify({"message": "works!"}), 200
