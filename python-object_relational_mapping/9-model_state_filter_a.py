#!/usr/bin/python3
"""task 9:
lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)
    result = query.filter(State.name.like("%a%")).order_by(State.id)

    for row in result:
        print(f"{row.id}: {row.name}")
