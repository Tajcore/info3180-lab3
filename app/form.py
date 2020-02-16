from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[Email(), DataRequired()])
    subject = StringField('subject', validators=[DataRequired()])
    message = TextAreaField('message', validators=[DataRequired()])
    
