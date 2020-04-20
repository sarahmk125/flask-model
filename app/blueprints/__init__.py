from app.blueprints import home
from app.blueprints import model


def init_app(app, blueprint):
    app.register_blueprint(blueprint)
