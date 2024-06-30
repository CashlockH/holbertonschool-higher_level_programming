#!/usr/bin/python3
"""Module"""

from model_state import Base, State
import SQLAlchemy
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    u = sys[1]
    p = sys[2]
    d_n = sys[3]
    qengine = create_engine(f'mysql+mysqldb://{u}:{p}@localhost/{d_n}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(state)
