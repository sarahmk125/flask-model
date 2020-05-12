import os
import app.utils.constants as constants
import app.utils.secrets as secrets

from app.models.models import FinancialModel, ModelParameter
from app.models.users import User


def init_app(app, db, environment):
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Init based on environment. Prod: use non-local DB
    if environment == constants.DEV_ENVIRONMENT_NAME:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{secrets.PROD_POSTGRES_USER}:{secrets.PROD_POSTGRES_PASS}@{secrets.PROD_POSTGRES_HOST}:{secrets.PROD_POSTGRES_PORT}/postgres'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
