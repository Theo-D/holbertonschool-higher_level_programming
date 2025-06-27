#!/usr/bin/python3
"""
Deletes states rows from which names contain the lette "a" from database.
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

    with Session() as session:
        with session.begin():
            states = session.query(State).filter(State.name.like("%a%")).all()
            for state in states:
                session.delete(state)
