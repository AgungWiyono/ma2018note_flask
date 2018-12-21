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
                'id' : fields.String(),
                'title' : fields.String(),
                'privacy': fields.String(),
                'author': fields.String(),
                'created': fields.DateTime()
                }
                )

# Note Edit Input
edit_note = api.model('Edit Note',
                     {
                         'title': fields.String(),
                         'body': fields.String,
                     }
                     )
