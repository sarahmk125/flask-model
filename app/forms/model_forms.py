from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length
from app.models.models import FinancialModel


class AddModelForm(FlaskForm):
    name = StringField('Model name', validators=[Length(0, 256), DataRequired()])
    version = StringField('Version', validators=[Length(0, 8), DataRequired()])

    submit = SubmitField('Submit')


class AddModelParameterForm(FlaskForm):
    model_unique_name = SelectField('Select Unique Model Name', choices=[])
    name = StringField('Parameter name', validators=[Length(0, 256), DataRequired()])
    value = FloatField('Parameter value (float)', validators=[DataRequired()])

    # Initialize with the model choices, called externally
    def __init__(self, models=None):
        super().__init__()
        if models:
            self.model_unique_name.choices = [(m.unique_name, m.unique_name) for m in models]

    submit = SubmitField('Submit')
