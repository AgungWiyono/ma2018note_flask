from flask import request
from flask_restplus import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity,\
        get_raw_jwt, create_access_token

from app.user import api
from app.user import serializers as s
from app.user import helpers as h

authorization = api.parser()
authorization.add_argument('Authorization', location='headers')

@api.route('/login')
class UserLogin(Resource):

    @api.expect(s.user_login)
    @api.marshal_with(s.login_success)
    def post(self):
        status = h.user_login(request.get_json())
        return status

