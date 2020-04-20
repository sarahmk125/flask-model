from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AddModelForm(FlaskForm):
    unique_name = StringField('Unique model name (typically [name]_[version])', validators=[Length(0, 256)])
    name = StringField('Model name', validators=[Length(0, 256)])
    version = StringField('Version', validators=[Length(0, 8)])

    submit = SubmitField('Submit')
