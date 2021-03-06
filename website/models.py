from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from .scripts import authScripts


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    data_created = db.Column(db.DateTime(timezone=True), default=func.now())
    confirm_acc = db.Column(db.Boolean, default=False)
    confirm_key = db.Column(
        db.String(128), default=authScripts.confirm_key_generator(size=100))
