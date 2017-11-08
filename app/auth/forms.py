from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo, Length
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    uname = StringField('Enter your uname', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'password_confirm', message='Passwords must match')])
    password_confirm = PasswordField(
        'Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')


def validate_email(self, data_field):
    if User.query.filter_by(email=data_field.data).first():
        raise ValidationError('There is an account with that email')


def validate_uname(self, data_field):
    if User.query.filter_by(uname=data_field.data).first():
        raise ValidationError('That uname is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
