from flask import jsonify
from profiler import app

from profiler.controllers.api.v1 import api_v1

@api_v1.route("/", methods=["GET"])
def api():

    result = {
        "profiler": "hello world"
    }

    return jsonify(result)