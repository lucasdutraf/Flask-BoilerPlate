from project.api.utils.creation_utils import Utils
from flask import jsonify, Blueprint
from database_singleton import Singleton

example_blueprint = Blueprint('example', __name__)
db = Singleton().database_connection()
utils = Utils()


@example_blueprint.after_request
def add_header(r):
    """
    Adding headers to prevent page caching
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0, post-check=0, pre-check=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "-1"
    return r


@example_blueprint.route('/ping', methods=['GET'])
def pong():
    return jsonify({"message": "works!"}), 200
