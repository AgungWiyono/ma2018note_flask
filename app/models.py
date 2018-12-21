from passlib.hash import pbkdf2_sha256 as sha256
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

from app import db


def to_dict(model):
    return { c.key: getattr(model, c.key)
            for c in inspect(model).mapper.column_attrs}

followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
                    )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    folders = db.relationship('Folder', backref='author', lazy='dynamic')
    password = db.Column(db.String())
    follow = db.relationship(
        'User', secondary = followers,
        primaryjoin = (followers.c.followed_id == id),
        secondaryjoin = (followers.c.follower_id == id),
        backref = db.backref('follower', lazy='dynamic'),
        lazy='dynamic')

    def __repr__(self):
        return self.name

    def follow(self, user):
        self.followed.append(user)
        db.session.commit()

    @classmethod
    def find_by_username(cls, name):
        return cls.query.filter_by(name=name).first()

    @staticmethod
    def hash_password(password):
        return sha256.hash(password)

    @staticmethod
    def verify_password(password, hash):
        return sha256.verify(password, hash)


class Privacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return self.name


class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20))
    privacy_id = db.Column(db.Integer, db.ForeignKey('privacy.id'))
    privacy = db.relationship('Privacy', backref='folders')
    created = db.Column(db.DateTime, nullable=False)
    notes = db.relationship('Note', backref='folder', lazy='dynamic')

    def __repr__(self):
        return '{} : {}'.format(self.author.name, self.name)

    @classmethod
    def foldername_exists(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_one_id(cls, id):
        return cls.query.filter_by(id=id).first()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '{}: {} => {}'.format(self.folder.author.name, self.folder.name, self.body)

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()
