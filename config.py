import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'app/static/images')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    AN_MAIL_SUBJECT_PREFIX = '[Antaenna Feedback]'
    AN_MAIL_SENDER = 'Antaenna Admin <soniabukirwa@yahoo.com>'   # Use Antaenna official
    AN_MAIL_RECEIVER = 'Antaenna Receiver <soniabukirwa@gmail.com>'  # Use Antaenna official
    AN_ADMIN = os.environ.get('AN_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite?check_same_thread=False')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite?check_same_thread=False')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': ProductionConfig,
}
