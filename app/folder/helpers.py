from datetime import datetime

from flask_restplus import abort
from flask_jwt_extended import get_jwt_identity

from app import db, to_dict
from app import User, Privacy, Folder, Note

def folder_list():
    datas = User.query.filter_by(name=get_jwt_identity()).first().folders
    result =[]
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
    if Folder.is_folder_exists(data['name']):
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
    folder = Folder.query.filter_by(id=id).first()
    if not folder:
        abort(404, 'Folder doesn\'t exists')

    result =[]
    for note in folder.notes:
        note_dict = to_dict(note)
        note_dict['url'] = note.id
        note_dict['author'] = note.folder.author.name
        note_dict['privacy'] = note.folder.privacy.name
        result.append(note_dict)
    return result
