import json
from flask_restful import Resource, request
from app.schemas import MessageSchema
from app.models.message import Message
from app.models.user import User


class MessageView(Resource):

    def post(self, user_id):
        """
        Create New Message
        """

        message_schema = MessageSchema()

        message_data = request.get_json()

         # Get User
        user = User.get_by_id(user_id)
        
        if not user:
            return dict(status='fail', message='User not found'), 404

        
        # Validate message data
        validated_message_data, errors = message_schema.load(message_data)

        if errors:
            return dict(status="fail", message=errors), 400

        message = Message(**validated_message_data)
        message.senderId = user_id
        saved_message = message.save()
        if not saved_message:
            return dict(status='fail', message=f'Internal Server Error'), 500

        # for returning message
        new_message_data, errors = message_schema.dumps(message)

        return dict(status='success', data=dict(message=json.loads(new_message_data))), 201


    def get(self, user_id):
        """
        Getting All Messages
        """

        message_schema = MessageSchema(many=True)

        # Get User
        user = User.get_by_id(user_id)
        
        if not user:
            return dict(status='fail', message='User not found'), 404

        messages = Message.find_all(senderId=user_id)

        messages_data, errors = message_schema.dumps(messages)

        if errors:
            return dict(status='fail', message=errors), 400

        return dict(
            status='success',
            data=dict(messages=json.loads(messages_data))
        ), 200
