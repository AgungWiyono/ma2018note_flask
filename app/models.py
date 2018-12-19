from flask_sqlalchemy import SQLAlchemy
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
    name = db.Column(db.String(20))
    folders = db.relationship('Folder', backref='author', lazy='dynamic')
    follow = db.relationship(
        'User', secondary = followers,
        primaryjoin = (followers.c.followed_id == id),
        secondaryjoin = (followers.c.follower_id == id),
        backref = db.backref('follower', lazy='dynamic'),
        lazy='dynamic')

    def __repr__(self):
        return self.name


class Privacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return self.name


class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(20))
    description = db.Column(db.String(20))
    privacy_id = db.Column(db.Integer, db.ForeignKey('privacy.id'))
    privacy = db.relationship('Privacy', backref='folders')
    created = db.Column(db.DateTime)
    notes = db.relationship('Note', backref='folder', lazy='dynamic')

    def __repr__(self):
        return '{} : {}'.format(self.author.name, self.name)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))
    body = db.Column(db.String())
    created = db.Column(db.DateTime)

    def __repr__(self):
        return '{}: {} => {}'.format(self.folder.author.name, self.folder.name, self.body)
