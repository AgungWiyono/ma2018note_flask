from datetime import datetime

from flask_restplus import abort
from flask_jwt_extended import get_jwt_identity

from app import db, to_dict
from app import User, Privacy, Folder, Note


error_404 = 'Folder doesn\'t exists'
error_401 = 'You don\'t have access to access this folder'

not_exists = lambda x: abort(404, error_404) if x is None else None
not_authorized = lambda x: abort(401, error_401) if x!=get_jwt_identity()\
                    else None

def folder_list():
    datas = User.query.filter_by(name=get_jwt_identity()).first().get_all_folders()
    for data in datas:
        data_dict = to_dict(data)
        data_dict['privacy'] = data.privacy.name
        data_dict['author'] = data.author.name
        data_dict['count'] = data.notes.count()
        data_dict['url'] = data.id
        result.append(data_dict)
    return result

def folder_post(data):
    username = User.find_by_username(get_jwt_identity())
    if Folder.foldername_exists(data['name']):
        abort(409, 'Foldername has been exists')
    data = Folder(name=data['name'],
                  description=data['description'],
                  privacy_id=data['privacy'],
                  created = datetime.utcnow()
                 )
    username.folders.append(data)
    db.session.commit()
    return {'message': 'Operation success'}, 201

def see_folder_notes(id):
    folder = Folder.get_one_id(id)

    not_exists(folder)
    not_authorized(folder.author.name)

    result =[]
    for note in folder.notes:
        note_dict = to_dict(note)
        note_dict['url'] = note.id
        note_dict['author'] = note.folder.author.name
        note_dict['privacy'] = note.folder.privacy.name
        result.append(note_dict)
    return result

def edit_folder(id, data):
    folder = Folder.get_one_id(id)

    not_exists(folder)
    not_authorized(folder.author.name)

    if data.get('name') :
        folder.name = data['name']
    if data.get('description'):
        folder.description = data['description']
    if data.get('privacy'):
        folder.privacy = data['privacy']

    db.session.commit()
    return {'message': 'Operation Success'}, 201

def delete_folder(id):
    folder = Folder.get_one_id(id)

    not_exists(folder)
    not_authorized(folder.author.name)

    db.session.delete(folder)
    db.session.commit()

    return {'message': 'Operation Success'}, 201

def post_notes(id, data):
    folder = Folder.get_one_id(id)

    not_exists(folder)
    not_authorized(folder.author.name)

    if Note.find_by_title(data['title']):
        abort(409, 'Title exists')

    note = Note(title=data['title'],
                body=data['body'],
                created=datetime.utcnow()
               )
    folder.notes.append(note)
    db.session.commit()

    return {'message': 'Operation Success'},201
