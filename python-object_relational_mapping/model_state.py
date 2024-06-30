#!/usr/bin/python3
"""Creating State Class"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            auto_increment=True,
            unique=True,
            nullable=False)
    name = Column(String(128), nullable=False)