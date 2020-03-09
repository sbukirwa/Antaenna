from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(client_id):
    return Client.query.get(int(client_id))


class Client(UserMixin, db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), nullable = False)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Broker %r>' % self.name


class Seller(UserMixin, db.Model):
    __tablename__ = 'sellers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    image = db.Column(db.LargeBinary, nullable=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128))
    medias = db.relationship('Media', backref='seller', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Broker %r>' % self.name


class Media(db.Model):
    __tablename__ = 'medias'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary, nullable=True)
    category_option = db.Column(db.String(32))
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'))