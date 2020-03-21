import json
from flask_restful import Resource, request
from app.schemas import UserSchema
from app.models.user import User


class UserSignup(Resource):

    def post(self):
        """
        Create New User
        """

        user_schema = UserSchema()

        user_data = request.get_json()
        
        # Validate user data
        validated_user_data, errors = user_schema.load(user_data)

        if errors:
            return dict(status="fail", message=errors), 400

        email = validated_user_data.get('email', None)

        # Check if user email exists
        user_existant = User.query.filter_by(email=email).first()

        if user_existant:
            return dict(status="fail", message=f"Email {validated_user_data['email']} already in use."), 400

        # add validated data to user object
        user = User(**validated_user_data)

        saved_user = user.save()

        if not saved_user:
            return dict(status='fail', message=f'Internal Server Error'), 500

        # for returning to user
        new_user_data, errors = user_schema.dumps(user)

        return dict(status='success', data=dict(user=json.loads(new_user_data))), 201


class UsersView(Resource):
    def get(self):
        """
        Getting All users
        """

        user_schema = UserSchema(many=True)

        users = User.find_all()

        users_data, errors = user_schema.dumps(users)

        if errors:
            return dict(status='fail', message=errors), 400

        return dict(
            status='success',
            data=dict(users=json.loads(users_data))
        ), 200

class UserlogIn(Resource):
    """
    User Login
    """
    def post(self):
        user_schema = UserSchema(only=("email", "password"))

        login_data = request.get_json()

        validated_user_data, errors = user_schema.load(login_data)

        if errors:
            return dict(status='fail', message=errors), 400
        
        email = validated_user_data.get('email', None)
        password = validated_user_data.get('password', None)

        user = User.find_first(email=email)

        if not user:
            return dict(status='fail', message="login failed, Wrong Email"), 401
        
        user_pass = user.password_is_valid(password)

        if not user_pass:
            return dict(status ='fail', message="login failed, Wrong Password"), 401

        user_data, errors = user_schema.dumps(user)

        if errors:
            return dict(status='fail', message=errors), 400

        return dict(status='Success', message=f"User { user.username } logged in Successfully. "), 200
User
class UserDetailView(Resource):

    def get(self, user_id):
        """
        Get specific user
        """
        user_schema = UserSchema()

        user = User.get_by_id(user_id)

        if not user:
            return dict(status='fail', message=f'User with id {user_id} does not exist'), 404

        user_data, errors = user_schema.dumps(user)

        if errors:
            return dict(status='fail', message=errors), 400
        
        return dict(status='success', data=dict(users=json.loads(user_data))), 200
        

    def patch(self, user_id):
        """
        Update User
        """
        user_schema = UserSchema()

        update_data = request.get_json()

        validated_update_data, errors = user_schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        user = User.get_by_id(user_id)

        if not user:
            return dict(status="fail", message=f"User with id {user_id} not found"), 404

        if 'username' in validated_update_data:
            user.username = validated_update_data['username']

        if 'email' in validated_update_data:
            user.email = validated_update_data['email']
        
        if 'password' in validated_update_data:
            user.password = validated_update_data['password']

        updated_user = user.save()

        if not updated_user:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status="success", message=f"User {user.username} updated successfully"), 200


    def delete(self, user_id):
        """
        Delete User
        """
        user = User.get_by_id(user_id)

        if not user:
            return dict(status="fail", message=f"User with id {user_id} not found"), 404

        deleted_user = user.delete()
        
        if not deleted_user:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(status='success', message="Successfully deleted"), 200
