#!/usr/bin/python3
"""Creating City Class"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """City class"""
    __tablename__ = "cities"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
