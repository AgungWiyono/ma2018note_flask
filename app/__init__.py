from flask import Flask, Blueprint
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


api = Api()
db = SQLAlchemy()
migrate = Migrate(compare_type=True)
admin = Admin(name='Muslim Note')

from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint, title='Note API')

    app.register_blueprint(blueprint)
    admin.init_app(app, endpoint='/api')

    return app

from .models import *

from .note.resources import api as noteApi

api.add_namespace(noteApi)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Privacy, db.session))
admin.add_view(ModelView(Folder, db.session))
admin.add_view(ModelView(Note, db.session))
