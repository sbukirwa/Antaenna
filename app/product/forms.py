from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, MultipleFileField, \
    SelectField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Email
from wtforms import ValidationError
from ..models import Product
from flask_wtf.file import FileAllowed, FileField, FileRequired


class AddProductsForm(FlaskForm):
    name = StringField("Store Name", validators=[DataRequired()])
    category_option = SelectField("Category :", choices=[('default', 'Choose Category'), ('Dresses', 'DRESSES'),
                                                             ('decorators', 'DECORATORS'), ('florists', 'FLORISTS'),
                                                             ('bakery', 'BAKERY'), ('tour & travel', 'TOUR & TRAVEL'),
                                                             ('venue', 'VENUES')])
    location = StringField("Location", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('Image 2', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('Image 3', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_4 = FileField('Image 4', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    submit = SubmitField("Submit")
