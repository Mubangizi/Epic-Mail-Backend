from flask_restful import Api

from app.controllers import (IndexView, UsersView, UserDetailView, UserlogIn)

api = Api()

# Index route
api.add_resource(IndexView, '/')

# User route
api.add_resource(UsersView, '/users', endpoint='user')
api.add_resource(UserDetailView, '/users/<int:user_id>')
api.add_resource(UserlogIn, '/login')
