#!/usr/bin/python3
"""Querying States with specific name"""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    d_n = sys.argv[3]
    state_name = sys.argv[4]
    if "'" in state_name:
        state_name = state_name.replace("'", "")
    engine = create_engine(f'mysql+mysqldb://{u}:{p}@localhost/{d_n}')
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")