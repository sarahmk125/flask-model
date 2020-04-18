import app.utils.constants as constants
from app import create_app


app = create_app()


if __name__ == "__name__":
    app.run(debug=constants.DEBUG)
