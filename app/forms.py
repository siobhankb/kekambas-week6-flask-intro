# need to run
# pip install flask-wtf

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    # no author needed here bc we set up foreign key in db to reference the User who made the post