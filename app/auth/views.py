import base64
from flask import render_template, flash, redirect, url_for, session, request, logging, send_file
from . import auth
from app import db
from app.models import Seller, Media
from .forms import LoginForm, RegistrationForm, MediaForm
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        seller = Seller(name=form.name.data, username=form.username.data, email=form.email.data,
                        password=form.password_hash.data)
        db.session.add(seller)
        db.session.commit()
        flash("You can now login.")
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
            if next is None or not next.startwith('/'):
                next = url_for('auth.home')
            return redirect(next)
        flash("Invalid username or password.")   # write the flash code in the template
    return render_template('auth/login.html', form=form)


@auth.route('/home', methods=["GET", "POST"])
def home():
    return render_template('auth/home.html')


@auth.route('/media/upload', methods=["GET", "POST"])
def media():
    form = MediaForm()
    if form.validate_on_submit():
        if not request.files["name"]:
            flash("You did not submit a file!")
            return render_template('auth/media_upload.html', form=form)

        files = request.files.getlist('name')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                media = Media(name=filename, data=file.read(), category_option=form.category_option.data)
                db.session.add(media)
                db.session.commit()
                flash("Media added!")
        return redirect(url_for('auth.downloads'))
    return render_template('auth/media_upload.html', form=form)


@auth.route('/downloads', methods=['POST', 'GET'])
def downloads():
    idn = 1
    db_images = []
    image = []
    image_no = db.session.query(Media.data).count()
    while idn <= image_no:
        db_images.append(Media.query.filter_by(id=idn).first())
        idn = idn + 1
    for img in db_images:
        image.append(base64.b64encode(img.data).decode("utf-8"))
    return render_template('auth/home.html', image=image)

