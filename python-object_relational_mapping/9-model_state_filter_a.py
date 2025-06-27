#!/usr/bin/python3
"""
Prints records containing letter "a" from the state table
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    a_state = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()\

    for state in a_state:
        print("{}: {}".format(state.id, state.name))
