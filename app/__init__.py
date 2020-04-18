import os
import app.lib.constants as constants

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configure the DB
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)


# Create all db tables
@app.before_first_request
def create_tables():
    # For some reason this wont work as a general import? To research.
    from models import Model, ModelParameter
    db.create_all()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.route("/")
def hello():
    return "Welcome to Flask!"


if __name__ == "__name__":
    app.run(debug=constants.DEBUG)
