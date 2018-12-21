import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG=True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
            'sqlite:///' + os.path.join( basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    PROPAGATE_EXCEPTIONS = True
    ERROR_INCLUDE_MESSAGE = False
    JWT_ERROR_MESSAGE_KEY='message'

    # For development only
    JWT_ACCESS_TOKEN_EXPIRES = False
