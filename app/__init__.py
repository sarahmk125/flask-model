import os

from flask import Flask
import app.utils.secrets as secrets

from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint


main = Blueprint('main', __name__)
db = SQLAlchemy()


def create_app():
    from . import models, blueprints

    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.FLASK_SECRET_STRING
    models.init_app(app, db)
    blueprints.init_app(app, main)

    return app
