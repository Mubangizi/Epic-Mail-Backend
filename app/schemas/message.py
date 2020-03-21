from marshmallow import Schema, fields, validate


class MessageSchema(Schema):

    id = fields.Integer(dump_only=True)

    subject = fields.String(required=True, error_message={
        "required": "subject is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='subject should be a valid string'
            ),
        ])
    message = fields.String(required=True, error_message={
        "required": "message is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='message should be a valid string'
            ),
        ])
    status = fields.String(
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='status should be a valid string'
            ),
        ])
    
    senderId = fields.Integer()
    createdOn = fields.DateTime()

    