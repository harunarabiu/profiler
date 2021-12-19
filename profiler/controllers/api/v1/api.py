from flask import jsonify, request
from profiler import app

from profiler.models.profile import Profile

from profiler.controllers.api.v1 import api_v1

@api_v1.route("/profiles", methods=["GET"])
def api():
    page = request.args.get('page', type=int)
    per_page = request.args.get('per_page', type=int)
    limit = request.args.get('limit', type=int)

    result = {
        "profiler": "hello world"
    }
    profile = Profile()
    return jsonify(profile.get_all(limit=limit, per_page=per_page, page=page)), 200