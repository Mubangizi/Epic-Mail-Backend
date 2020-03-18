import json
from flask_restful import Resource, request
from app.schemas import UserSchema
from app.models.user import User


class UsersView(Resource):

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

        # add validated vdata to user object
        user = User(**validated_user_data)

        saved_user = user.save()

        if not saved_user:
            return dict(status='fail', message=f'Internal Server Error'), 500

        # for returning to user
        new_user_data, errors = user_schema.dumps(user)

        return dict(status='success', data=dict(user=json.loads(new_user_data))), 201



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
