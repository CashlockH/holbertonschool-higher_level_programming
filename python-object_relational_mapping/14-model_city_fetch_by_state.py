#!/usr/bin/python3
"""Querying City objects"""
from model_state import Base, State
from model_city import City
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
    states = session.query(State, City).filter(State.id==City.state_id).order_by(City.id)
    for state in states:
        print("{}: ({}) {}".format(state.State.name, state.City.id, state.City.name))
