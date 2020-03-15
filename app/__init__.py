from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class

photos = UploadSet('photos', IMAGES)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_view = 'main.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.debug = False
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    configure_uploads(app, photos)
    patch_request_class(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .product import product as product_blueprint
    app.register_blueprint(product_blueprint, url_prefix='/product')

    return app
