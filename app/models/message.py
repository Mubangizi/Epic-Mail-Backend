from flask_bcrypt import Bcrypt
from datetime import timedelta

from ..models import db

from app.models.base_model import BaseModel


class Message(BaseModel):
    """ message table definition """

    _tablename_ = "message"

    # fields of the message table
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(256), nullable=False, default="")
    message = db.Column(db.String(256), nullable=False, default="")
    status = db.Column(db.String(256), nullable=False, default="draft")
    parentMessageId = db.Column(db.Integer, nullable=True)
    createdOn = db.Column(db.DateTime, default=db.func.current_timestamp())
    senderId = db.Column(db.Integer, db.ForeignKey('user.id'))



    def __init__(self, subject, message):
        """ initialize message """
        self.subject = subject
        self.message = message


    def __repr__(self):
        return "<Message: {}>".format(self.subject)
