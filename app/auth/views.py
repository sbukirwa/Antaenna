from flask import render_template, flash, redirect, url_for, session, request, logging, send_file
from . import auth
from app import db
from app.models import Seller, Product
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required, current_user


# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'])


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        file = request.files['image']
        if file:
            seller = Seller(image=file.read(), name=form.name.data, username=form.username.data, email=form.email.data,
                            password=form.password_hash.data)
            db.session.add(seller)
            db.session.commit()
            flash('Welcome {form.name.data} ,You can now login.', 'Success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        seller = Seller.query.filter_by(email=form.email.data).first()
        if seller is not None and seller.verify_password(form.password_hash.data):
            login_user(seller, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startwith('/product/addproduct'):
                next = url_for('auth.homepage')
            return redirect(next)
        flash("Invalid username or password.")   # write the flash code in the template
    return render_template('auth/login.html', form=form)


@auth.route('/home', methods=["GET", "POST"])
def home():
    seller = current_user
    product = Product.query.filter_by(seller_id=current_user.id).first()
    product_dict = dict((col, getattr(product, col)) for col in product.__table__.columns.keys())
    return render_template('auth/home.html', product_dict = product_dict, product=product)


@auth.route('/homepage', methods=["GET", "POST"])
def homepage():
    return render_template('auth/homepage.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('auth.login'))


