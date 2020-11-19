from datetime import datetime
from app import db


class User(db.Model):
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)
