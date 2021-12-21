import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from flask_migrate import Migrate  # type: ignore
from flask_marshmallow import Marshmallow
from flask_caching import Cache

from .errorhandlers import unhandled_exception, internal_server_error, page_not_found

app = Flask(__name__)

APP_STATUS = os.getenv('PROFILER_STATUS')
print(APP_STATUS)
app.config.from_object(APP_STATUS)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
cache = Cache(app)
cache.init_app(app)

from .controllers.api.v1 import api_v1
from .controllers.docs import api_doc
from .models.profile import Profile
from . import commands

app.register_blueprint(api_doc, url_prefix="/")
app.register_blueprint(api_v1, url_prefix="/api/v1")


app.register_error_handler(Exception, unhandled_exception)
app.register_error_handler(500, internal_server_error)
app.register_error_handler(404, page_not_found)

#print(app.url_map)
