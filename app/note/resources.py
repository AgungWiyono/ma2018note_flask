from flask import request
from flask_restplus import Resource
from flask_jwt_extended import jwt_required

from app.note import api
from app.note import helpers as h
from app.note import serializers as s

authorization = api.parser()
authorization.add_argument('Authorization', location='headers')

@api.route('/<id>')
class Note(Resource):

    @jwt_required
    @api.marshal_with(s.note)
    @api.doc(description='Show a content of a note',
             params={'id': 'Note ID'},
             parser=authorization)
    def get(self, id):
        data = h.read_note(id)
        return data

    @jwt_required
    @api.marshal_with(s.general_message)
    @api.doc(description='Edit attributes of a note',
             parser=authorization,
             params={'id': 'Note ID'},
             body = s.edit_note)
    def put(self, id):
        status = h.edit_note(id, request.get_json())
        return status

    @jwt_required
    @api.marshal_with(s.general_message)
    @api.doc(description='Delete a note',
             parser=authorization,
             params={'id': 'Note ID'})
    def delete(self, id):
        status = h.delete_note(id)
        return status
