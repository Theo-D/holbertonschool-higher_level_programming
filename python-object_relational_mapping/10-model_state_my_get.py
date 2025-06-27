#!/usr/bin/python3
"""
Prints the state from database which name was given as argument
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    name_arg = sys.argv[4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == name_arg).first()

    if state:
        print(state.id)
    else:
        print("Not found")
