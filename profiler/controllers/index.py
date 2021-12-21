from flask import Blueprint
index = Blueprint("index", __name__)

@index.route("/")
def index():

    return "<h1>Welcome to Profiler"