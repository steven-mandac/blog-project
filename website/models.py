from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    birth_date = db.Column(db.String(150), default="dd-MM-YYYY")
    posts = relationship('ShitPost')


class ShitPost(db.Model):
    __tablename__ = 'shitposts'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.ForeignKey('users.id'))
    