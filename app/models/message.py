from flask_bcrypt import Bcrypt
from datetime import timedelta

from ..models import db

from app.models.parent_model import ParentModel


class Message(ParentModel):
    """ message table definition """

    _tablename_ = "message"

    # fields of the message table
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(256), nullable=False, default="")
    message = db.Column(db.String(256), nullable=False, default="")
    status = db.Column(db.String(256), nullable=False, default="")
    parentMessageId = db.Column(db.Integer, primary_key=True)
    createdOn = db.Column(db.DateTime, default=db.func.current_timestamp())


    def __init__(self, subject, message, parentMessageId):
        """ initialize message """
        self.subject = subject
        self.message = message
        self.parentMessageId = parentMessageId


    def __repr__(self):
        return "<Message: {}>".format(self.subject)
