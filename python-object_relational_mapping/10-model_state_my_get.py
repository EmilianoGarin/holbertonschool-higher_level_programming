#!/usr/bin/python3
"""task 10:
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)
    result = query.filter(State.name.like(sys.argv[4])).order_by(State.id)

    if len(list(result)) == 0:
        print("Not found")
    else:
        for row in result:
            print(f"{row.id}")
