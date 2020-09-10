from flask_wtf  import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email, Length

class EmailSignupForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Enter a valid email'),Length(max=60)])
