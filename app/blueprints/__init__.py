from app.blueprints import home
from app.blueprints import model
from app.blueprints import auth


def init_app(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
