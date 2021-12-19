from flask import jsonify, request
from profiler import app, cache

from profiler.models.profile import Profile

from profiler.controllers.api.v1 import api_v1

@api_v1.route("/profiles", methods=["GET"])
@cache.cached(300, query_string=True) # Cache request with args for 300 seconds
def api():
    page = request.args.get('page', type=int)
    per_page = request.args.get('per_page', type=int)
    limit = request.args.get('limit', type=int)

    gender = request.args.get('gender', type=str)
    title = request.args.get('title', type=str)
    nationality = request.args.get('nationality', type=str)
    
    profile = Profile()

    if gender or title or nationality:
        result = profile.filter_by_columns(limit=limit, per_page=per_page, page=page, gender=gender, title=title, nationality=nationality)
    else:
        result = profile.get_all(limit=limit, per_page=per_page, page=page)


    return jsonify(result), 200