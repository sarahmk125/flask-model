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


# # Create all db tables
# @app.before_first_request
# def create_tables():
#     # For some reason this wont work as a general import? To research.
#     from models import Model, ModelParameter
#     db.create_all()


# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db)
