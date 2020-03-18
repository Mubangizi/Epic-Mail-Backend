from flask_restful import Api

from app.controllers import (IndexView, UsersView)

api = Api()

# Index route
api.add_resource(IndexView, '/')

# User route
api.add_resource(UsersView, '/users', endpoint='user')
