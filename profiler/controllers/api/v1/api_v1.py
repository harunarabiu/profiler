from flask import jsonify, request
from profiler import app

@app.route('/api')
def api_v1():

    result = {
        "profiler": "hello world"
    }

    return jsonify(result)