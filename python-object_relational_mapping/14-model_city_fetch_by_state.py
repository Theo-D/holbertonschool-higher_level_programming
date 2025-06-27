#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa:
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
            rec = session.query(State.name, City.id, City.name)\
                         .join(City, City.state_id == State.id)\
                         .order_by(City.id)\
                         .all()
            for state_name, city_id, city_name in rec:
                print("{}: ({}) {}".format(state_name, city_id, city_name))
