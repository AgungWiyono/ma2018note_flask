from flask_restplus import Resource

from app.note import api
from app.note import serializers as s


@api.route('/<id>')
class Note(Resource):

    @api.marshal_with(s.note)
    @api.doc(description='Show a content of a note', params={'id': 'Note ID'})
    def get(self, id):
        pass

    @api.marshal_with(s.general_message)
    @api.doc(description='Edit attributes of a note', params={'id': 'Note ID'})
    def put(self, id):
        pass

    @api.marshal_with(s.general_message)
    @api.doc(description='Delete a note', params={'id': 'Note ID'})
    def delete(self, id):
        pass
