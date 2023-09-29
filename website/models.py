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
    posts = relationship('ShitPost', back_populates='user')
    comments = relationship('Comment', back_populates='comment_author')


class ShitPost(db.Model):
    __tablename__ = 'shitposts'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user = relationship('User', back_populates='posts')
    user_id = db.Column(db.ForeignKey('users.id'))
    
    comments = relationship('Comment', back_populates='parent_post')
    
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.ForeignKey('users.id'))
    comment_author = relationship('User', back_populates='comments')
    
    post_id = db.Column(db.ForeignKey('shitposts.id'))
    parent_post = relationship('ShitPost', back_populates='comments')
    text = db.Column(db.String(250), nullable=False)