#!/usr/bin/python3
"""
Lists the first State object.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    session = sessionmaker()(bind=engine)

    state = session.query(State).order_by(State.id).first()
    if state:
        print(state)
    else:
        print("Nothing")
    session.close()