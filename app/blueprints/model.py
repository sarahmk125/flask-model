from app import main
from app import db
from app.forms.model_forms import AddModelForm
from flask import redirect, url_for, render_template
from flask_login import login_required
from app.models.models import FinancialModel


@main.route('/add-model', methods=['GET', 'POST'])
@login_required
def add_model():
    name = None
    version = None
    unique_name = None
    form = AddModelForm()
    if form.validate_on_submit():
        # Need to make sure these are required?
        # Construct the model
        financial_model = FinancialModel(
            name=form.name.data,
            version=form.version.data,
            unique_name=form.unique_name.data
        )

        # Save the model to the DB
        db.session.add(financial_model)
        db.session.commit()

        return redirect(url_for('main.add_model'))

    return render_template('add_model.html', form=form)


@main.route('/view-models', methods=['GET'])
@login_required
def view_models():
    all_models = FinancialModel.query.all()
    return render_template('view_models.html', data=all_models)
