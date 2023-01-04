from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config

# create a Flask obj, use __name__ for other files and templates.
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from core import routes