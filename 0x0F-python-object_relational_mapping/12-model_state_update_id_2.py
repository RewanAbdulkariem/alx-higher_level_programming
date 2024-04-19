#!/usr/bin/python3
"""
Inserts a new State into the database.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    session = sessionmaker()(bind=engine)

    update_state = session.query(State).filter(State.id == 2).first()

    update_state.name = "New Mexico"
    session.commit()
    session.close()
