from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from datetime import datetime
import simplejson as json

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key = True)
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime())
    last_login = db.Column(db.DateTime())
    active = db.Column(db.Boolean)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    pass_hash = db.Column(db.String(255))
    email_key = db.Column(db.String(15))


class err404(db.Model):
    __tablename__ = 'err404'
    error_id = db.Column(db.Integer(), primary_key=True)
    path = db.Column(db.String(200))
    occurrences = db.Column(db.Integer)
    first_occurred = db.Column(db.DateTime)
    last_occurred = db.Column(db.DateTime)
