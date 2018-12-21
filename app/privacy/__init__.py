from flask_restplus import Namespace, Resource, fields

from app import Privacy


api = Namespace('privacy', description='See all privacy item')

# Privacy schema
privacySch = api.model('Privacy List',
                      {
                          'id': fields.Integer(description='Privacy id number'),
                          'name': fields.String(description='Privacy name')
                      }
                      )

@api.route('')
class privacy(Resource):

    @api.marshal_with(privacySch)
    def get(self):
        data = Privacy.query.all()
        return data
