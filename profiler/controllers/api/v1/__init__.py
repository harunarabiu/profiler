from flask import Blueprint

api_v1 = Blueprint("api_v1", __name__)

from profiler.controllers.api.v1.api import api  # noqa: F401 E402


@api_v1.before_request
def api_v1_before_request():
    """This will occur after the application's 'before request' has been called."""
    pass


@api_v1.after_request
def api_v1_after_request(response):
    """This will occur after the application's 'after request' has been called."""
    return response