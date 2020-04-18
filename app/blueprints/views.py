from app import main


@main.route('/')
def hello():
    return "Welcome to Flask!"
