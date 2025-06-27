#!/usr/bin/python3
"""
Updates name to "New-Mexico" on row with id = 2 from the table state
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
            state = session.query(State).filter_by(id=2).first()
            if state:
                state.name = "New Mexico"
