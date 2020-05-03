from app import main
from app import db
from app.forms.model_forms import AddModelForm, AddModelParameterForm
from flask import redirect, url_for, render_template
from flask_login import login_required
from app.models.models import FinancialModel, ModelParameter


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
            unique_name=form.name.data + '__' + form.version.data
        )

        # Save the model to the DB
        db.session.add(financial_model)
        db.session.commit()

        return redirect(url_for('main.add_model'))

    return render_template('add_model.html', form=form)


@main.route('/add-model-parameter', methods=['GET', 'POST'])
@login_required
def add_model_parameter():
    model_unique_name = None
    unique_name = None
    name = None
    value = None
    form = AddModelParameterForm()
    if form.validate_on_submit():
        # Need to make sure these are required?
        # First, get the model id for the model unique name
        # NOTE: Add error handling here
        model_obj = FinancialModel.query.filter_by(unique_name=form.model_unique_name.data).first()
        model_id = model_obj.id

        # Construct the model parameters; unique name is model name + param name        
        model_parameter = ModelParameter(
            model_id = model_id,
            name=form.name.data,
            value=form.value.data,
            unique_name=form.model_unique_name.data + '__' + form.name.data
        )

        # Save the model to the DB
        db.session.add(model_parameter)
        db.session.commit()

        return redirect(url_for('main.add_model_parameter'))

    return render_template('add_model_parameter.html', form=form)


@main.route('/view-models', methods=['GET'])
@login_required
def view_models():
    all_models = FinancialModel.query.all()
    return render_template('view_models.html', data=all_models)
