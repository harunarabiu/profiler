import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from flask_migrate import Migrate  # type: ignore
from flask_marshmallow import Marshmallow

app = Flask(__name__)

APP_STATUS = os.getenv('PROFILER_STATUS')
print(APP_STATUS)
app.config.from_object(APP_STATUS)




db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from .controllers.api.v1 import api_v1
from .models.profile import Profile
from . import commands

app.register_blueprint(api_v1, url_prefix="/api/v1")
#print(app.url_map)
