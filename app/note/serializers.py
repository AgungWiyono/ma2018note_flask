from flask_restplus import fields
from flask import request
from app.note import api


# For general message
general_message = api.model('General Message',
                           {
                               'message': fields.String(description='Message for general purpose')
                           }
                           )


# Read a note
note = api.model('Read a note',
                {
                'id' : fields.String(description='Link to folder. Based on ID'),
                'name' : fields.String(description="Folder's name"),
                'privacy': fields.String(description="Folder's privacy"),
                'author': fields.String(description='Folder\'s author'),
                'created': fields.DateTime(description='Date Created'),
                'count': fields.Integer(description='Notes in folder')
                }
                )
