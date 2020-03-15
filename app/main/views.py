from flask import render_template, redirect, url_for, request, flash
from app import db
from app.models import Client, Seller
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from . import main


@main.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')


@main.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        client = Client(name=form.name.data, email=form.name.data, username=form.username.data,
                        password=form.password_hash.data)
        db.session.add(client)
        db.session.commit()
        flash("You can now login.")
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form, title="Login")


@main.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        client = Client.query.filter_by(username=form.username.data).first()
        if client is not None and client.verify_password(form.password_hash.data):
            login_user(client, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startwith('/'):
                next = url_for('main.home')
            return redirect(next)
        flash("Invalid username or password.")   # write the flash code in the template
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('auth.login'))
