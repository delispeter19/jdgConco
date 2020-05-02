from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date (YYYY-MM-DD)', format='%Y-%m-%d')
    fb_link = StringField('Facebook Link', validators=[DataRequired()])
    imgFile = FileField('Image File', validators=[FileAllowed(['jpg', 'png'])])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')