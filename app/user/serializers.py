from flask_restplus import fields

from app.user import api

# User login
user_login = api.model('User Login',
                      {
                          'name': fields.String(required=True, description='Registered Username'),
                          'password': fields.String(required=True)
                      }
                      )

# Login success message
login_success = api.model('Login Success',
                         {
                             'username': fields.String(),
                             'token': fields.String(description='access token')
                         }
                         )

# General message
general_message = api.model('General Message',
                           {
                               'message': fields.String
                           }
                           )
