from app.models import User
from flask_restplus import abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token

db = SQLAlchemy()

def user_login(data):
    name = data.get('name')
    password = data.get('password')

    user = User.query.filter_by(name=name).first()
    if not user:
        print('user exists')
        abort(404, 'User doesn\'t exists')

    if User.verify_password(password, user.password):
        access_token = create_access_token(identity= name)
        print('password is right')
    else:
        abort(403, 'Password isn\'t correct')
        print('password is wrong')

    return {
        'username': name,
        'token': access_token
    }
