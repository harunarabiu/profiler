import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

APP_STATUS = os.getenv('PROFILER_STATUS')

app.config.from_object(APP_STATUS)




db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .controllers.api.v1 import api_v1
from .models import *

app.register_blueprint(api_v1, url_prefix="/api/v1")