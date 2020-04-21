from app import main
from app.forms.model_forms import AddModelForm
from flask import render_template
from flask import redirect, url_for


@main.route('/')
def home():
    return render_template('home.html')
