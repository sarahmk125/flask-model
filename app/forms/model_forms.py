from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AddModelForm(FlaskForm):
    name = StringField('Model name', validators=[Length(0, 256), DataRequired()])
    version = StringField('Version', validators=[Length(0, 8), DataRequired()])
    
    submit = SubmitField('Submit')


class AddModelParameterForm(FlaskForm):
    model_unique_name = StringField('Unique model name (typically [name]__[version])', validators=[Length(0, 256), DataRequired()])
    name = StringField('Parameter name', validators=[Length(0, 256), DataRequired()])
    value = StringField('Parameter value (float)', validators=[DataRequired()])

    submit = SubmitField('Submit')