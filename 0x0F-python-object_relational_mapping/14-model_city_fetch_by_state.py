#!/usr/bin/python3
"""Lists City objects"""

import sys
from model_city import City
from model_state import Base, State

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = db.create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Sess = sessionmaker(bind=engine)
    session = Sess()
    result = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")
