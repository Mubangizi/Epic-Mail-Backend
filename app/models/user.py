from flask_bcrypt import Bcrypt
from datetime import timedelta

from ..models import db

from app.models.parent_model import ParentModel


class User(ParentModel):
    """ user table definition """

    _tablename_ = "users"

    # fields of the user table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True, nullable=False, default="")
    username = db.Column(db.String(256), nullable=False, default="")
    password = db.Column(db.String(256), nullable=False, default="")
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


    def __init__(self, email, username, password):
        """ initialize with email, username and password """
        self.email = email
        self.username = username
        self.password = Bcrypt().generate_password_hash(password).decode()

    def password_is_valid(self, password):
        """ checks the password against it's hash to validate the user's password """
        return Bcrypt().check_password_hash(self.password, password)


    def __repr__(self):
        return "<User: {}>".format(self.email)
