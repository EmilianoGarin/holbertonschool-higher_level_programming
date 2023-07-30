#!/usr/bin/python3
"""task 12:
changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine(
        f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)
    session = Session()

    test = update(State).where(State.id == 2).values(name="New Mexico")
    session.execute(test)
    session.commit()
