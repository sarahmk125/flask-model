import os

from flask import Flask
import app.utils.secrets as secrets

from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask_login import LoginManager


main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)
db = SQLAlchemy()


def create_app():
    from . import models, blueprints

    app = Flask(__name__)

    # Init models and blueprints
    app.config['SECRET_KEY'] = secrets.FLASK_SECRET_STRING
    models.init_app(app, db)
    blueprints.init_app(app, [auth, main])

    # Establish login procedure
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return models.users.User.query.get(int(user_id))

    return app
