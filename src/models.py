import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
import enum 
from sqlalchemy import Integer, Enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship("User")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship("User")

class TypeEnum(enum.Enum):
    image=1
    text=2

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type= Column(Enum(TypeEnum))
    url= Column(String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    post = relationship("Post")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(256), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship("User")
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    post = relationship("Post")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e