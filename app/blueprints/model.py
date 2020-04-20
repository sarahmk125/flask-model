from app import main
from app.forms.model_forms import AddModelForm
from flask import render_template
from flask import redirect, url_for


@main.route('/add-model', methods=['GET', 'POST'])
def add_model():
    name = None
    version = None
    unique_name = None
    form = AddModelForm()
    if form.validate_on_submit():
        name = form.name.data
        version = form.version.data
        unique_name = form.unique_name.data
        return redirect(url_for('main.add_model'))

    return render_template('add_model.html', form=form)
