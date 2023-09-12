#!/usr/bin/python3
"""task 12:
changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine(
        f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City)
    result = query.join(City, State.id == City.state_id).all()

    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
