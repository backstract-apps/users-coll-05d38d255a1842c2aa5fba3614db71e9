from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    description = Column(String, primary_key=False)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String, primary_key=False)
    lastname = Column(String, primary_key=False)

