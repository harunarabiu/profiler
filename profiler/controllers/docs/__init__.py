from flask import Blueprint, render_template, request
from urllib.parse import urlparse

api_doc = Blueprint('api_doc', __name__)


@api_doc.route("/", methods=["GET"])
def doc():
    host_name = urlparse(request.base_url)
    host_name = host_name.netloc

    return  render_template("index.html", host=host_name)
