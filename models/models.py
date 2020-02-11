from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class PoemContent(Base):
    __tablename__ = 'poemcontents'
    id = Column(Integer, primary_key=True)
    title = Column(String(64), unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title: %r>' % self.title


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(64), unique=True)
    hashed_pass = Column(String(64))

    def __init__(self, user_name=None, hashed_pass=None):
        self.user_name = user_name
        self.hashed_pass = hashed_pass

    def __repr__(self):
        return '<Name: %r>' % self.user_name
