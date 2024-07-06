#!/usr/bin/python3
"""Querying States with a"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    d_n = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{u}:{p}@localhost/{d_n}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
        else:
            pass
