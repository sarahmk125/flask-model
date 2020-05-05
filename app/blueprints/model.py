import app.utils.constants as constants
import logging

from app import main
from app import db
from app.forms.model_forms import AddModelForm, AddModelParameterForm
from flask import redirect, url_for, render_template, flash, request
from flask_login import login_required
from app.models.models import FinancialModel, ModelParameter
from app.utils.helpers import form_throw_error


@main.route('/add-model', methods=['GET', 'POST'])
@login_required
def add_model():
    name = None
    version = None
    unique_name = None
    form = AddModelForm()

    logging.info(f'[Blueprint.Model.add_model] Form data entered: name = {form.name.data}, version = {form.version.data}...')
    if not form.validate_on_submit() and request.method=='POST':
        form_throw_error('[Blueprint.Model.add_model]', form, constants.DATA_MISSING_MESSAGE)
        return render_template('add_model.html', form=form)

    if form.validate_on_submit():
        # Construct the model
        logging.info(f'[Blueprint.Model.add_model] Adding model with form data...')
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
    # First, get all models to initialize model name dropdown in form
    all_models = FinancialModel.query.all()

    model_unique_name = None
    unique_name = None
    name = None
    value = None
    form = AddModelParameterForm(all_models)

    logging.info(f'[Blueprint.Model.add_model_parameter] Form data entered: model_unique_name = {form.model_unique_name.data}, name = {form.name.data}, value = {form.value.data}...')

    if not form.validate_on_submit() and request.method=='POST':
        form_throw_error('[Blueprint.Model.add_model_parameter]', form, constants.DATA_MISSING_MESSAGE)
        return render_template('add_model_parameter.html', form=form)

    if form.validate_on_submit():
        model_obj = FinancialModel.query.filter_by(unique_name=form.model_unique_name.data).first()
        if not model_obj:
            flash(f"No model found with unique name '{form.model_unique_name.data}'.")
            return render_template('add_model_parameter.html', form=form)

        # Model is found, continue
        model_id = model_obj.id

        # Construct the model parameters; unique name is model name + param nametry
        logging.info(f'[Blueprint.Model.add_model_parameter] Adding model parameter with form data...')
        model_parameter = ModelParameter(
            model_id=model_id,
            name=form.name.data,
            value=form.value.data,
            unique_name=form.model_unique_name.data + '__' + form.name.data
        )

        # Save the model to the DB
        db.session.add(model_parameter)
        db.session.commit()

        return redirect(url_for('main.add_model_parameter'))

    return render_template('add_model_parameter.html', form=form)


@main.route('/clear-models', methods=['GET', 'POST'])
@login_required
def clear_models():
    logging.info(f'[Blueprint.Model.clear_models] Attempting to clear all models...')
    try:
        db.session.query(FinancialModel).delete()
        db.session.query(ModelParameter).delete()
        db.session.commit()
    except Exception as e:
        flash("Unknown error: could not clear models")
        return redirect(url_for('main.view_models'))
    return redirect(url_for('main.home'))


@main.route('/clear-model-parameters', methods=['GET', 'POST'])
@login_required
def clear_model_parameters():
    logging.info(f'[Blueprint.Model.clear_model_parameters] Attempting to clear all model parameters...')
    try:
        db.session.query(ModelParameter).delete()
        db.session.commit()
    except Exception as e:
        flash("Unknown error: could not clear model parameters")
    return redirect(url_for('main.view_models'))


@main.route('/view-models', methods=['GET'])
@login_required
def view_models():
    logging.info(f'[Blueprint.Model.view_models] Attempting to view all models...')
    all_models = FinancialModel.query.all()
    return render_template('view_models.html', data=all_models)


@main.route('/view-model-parameters', methods=['GET'])
@login_required
def view_model_parameters():
    logging.info(f'[Blueprint.Model.view_model_parameters] Attempting to view all model parameters...')
    all_parameters = ModelParameter.query.all()
    return render_template('view_model_parameters.html', data=all_parameters)
