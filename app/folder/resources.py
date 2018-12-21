from pprint import pprint

from flask import request
from flask_restplus import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.folder import api
from app.folder import serializers as s
from app.folder import helpers as h

authorization = api.parser()
authorization.add_argument('Authorization', location='headers')

@api.route('')
class FolderList(Resource):

    @jwt_required
    @api.marshal_with(s.folder_list)
    @api.doc(description='Show all user\'s own folder', parser=authorization)
    def get(self):
        data = h.folder_list()
        return data

    @jwt_required
    @api.marshal_with(s.general_message)
    @api.doc(description='Create a new folder',
             parser=authorization,
             body=s.new_folder)
    def post(self):
        data = request.get_json()
        result = h.folder_post(data)
        return result


@api.route('/<id>')
class Folder(Resource):

    @jwt_required
    @api.marshal_with(s.folder_notes)
    @api.doc('See all notes in a folder',
             params={'id': 'Folder ID'},
             parser=authorization)
    def get(self, id):
        data = h.see_folder_notes(id)
        return data

    @jwt_required
    @api.marshal_with(s.general_message)
    @api.doc(description='Edit folder attribute',
             params={'id': 'Folder ID'},
             parser=authorization,
             body=s.edit_folder)
    def put(self, id):
        status = h.edit_folder(id, request.get_json())
        return status

    @jwt_required
    @api.marshal_with(s.general_message)
    @api.doc(description='Delete a folder, along with its contents',
             params={'id': 'Folder ID'},
             parser=authorization)
    def delete(self, id):
        status = h.delete_folder(id)
        return status

    @jwt_required
    @api.marshal_with(s.general_message)
    @api.doc(description='Post a new note',
            parser=authorization,
            body=s.new_note)
    def post(self, id):
        status = h.post_notes(id, request.get_json())
        return status
