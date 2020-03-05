from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, MultipleFileField, \
    SelectField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Email
from wtforms import ValidationError
from ..models import Seller, Media


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


def validate_username(self, field):
        if Seller.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password_hash = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log In")


class MediaForm(FlaskForm):
    name = MultipleFileField("Upload Images :", validators=[DataRequired()])
    category_option = SelectField("Category :", choices=[('default', 'Choose Lease type'), ('Dresses', 'DRESSES'),
                                                         ('decorators', 'DECORATORS'), ('florists', 'FLORISTS'),
                                                         ('bakery', 'BAKERY'), ('tour & travel', 'TOUR & TRAVEL'),
                                                         ('venue', 'VENUES')])
    submit = SubmitField("Submit")
