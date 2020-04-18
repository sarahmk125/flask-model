from app.blueprints import views


def init_app(app, blueprint):
    app.register_blueprint(blueprint)
