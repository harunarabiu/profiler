from flask import jsonify


def unhandled_exception(error):
    result = {
        "error": "oops, something has gone wrong."
    }

    return jsonify(result), 500

def internal_server_error(e):
    result = {
        "error": "oops, something has gone wrong."
    }
    # note that we set the 500 status explicitly
    return jsonify(result), 500

def page_not_found(e):
    result = {
        "error": "endpoint not found."
    }
    return jsonify(result), 404