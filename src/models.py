import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(70), nullable=False, unique=True)

    follower = relationship('Followers', back_populates='user')



class Followers(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('Users',back_populates='follower')

class Post(Base):
    __tablename__="post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    author = relationship('Users', back_populates='post') 

class Comment(Base):
    __tablename__="comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200))
    author_id = Column(Integer,ForeignKey('users.id'))
    post_id = Column(Integer,ForeignKey('post.id'))

    author_comment= relationship('Users',back_populates='comment')
    author_post= relationship('Post',back_populates='comment' )

class Media(Base):
    __tablename__="media"
    id = Column(Integer, primary_key=True)
    type = Column(String(20))
    url = Column(String(100))
    post_id = Column(Integer, ForeignKey('post.id'))

    owner_post = relationship('Post',back_populates='media')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
