from pprint import pprint

from flask_restplus import abort
from flask_jwt_extended import get_jwt_identity

from app import db, to_dict
from app.models import User, Note

error_404 = 'Note doesn\'t exists'
error_401 = 'You don\'t have access to this folder'

not_exists = lambda x: abort(404, error_404) if x is None else None
not_authorized = lambda x: abort(401, error_401) if x!=get_jwt_identity()\
                 else None

def read_note(id):
    note = Note.find_by_id(id)

    not_exists(note)
    not_authorized(note.folder.author.name)

    note_dict = to_dict(note)
    note_dict['privacy'] = note.folder.privacy.name
    note_dict['author'] = note.folder.author.name

    return note_dict

def edit_note(id, data):
    note = Note.find_by_id(id)

    not_exists(note)
    not_authorized(note.folder.author.name)


    if data.get('title'):
        if Note.find_by_title(data['title']):
            abort(409, 'Title exists')
        note.title = data['title']

    if data.get('body'):
        note.body = data['body']

    db.session.commit()

    return {'message': 'Operation Success'},200

def delete_note(id):
    note = Note.find_by_id(id)

    not_exists(note)
    not_authorized(note.folder.author.name)

    db.session.delete(note)
    db.session.commit()

    return {'message': 'Operation success'}, 201
