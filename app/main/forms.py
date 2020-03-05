from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Email
from wtforms import ValidationError
from ..models import Client, Seller


class RegistrationForm(FlaskForm):
    name = StringField('Full name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                         'Usernames must have only '
                                                                                         'letters, numbers, dots or ' 
                                                                                         'underscores')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2',
                                                                             message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Client.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if Client.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class LoginForm(FlaskForm):
    username = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')