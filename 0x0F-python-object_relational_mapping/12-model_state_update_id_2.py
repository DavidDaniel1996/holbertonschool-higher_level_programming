#!/usr/bin/python3
"""Changes state id=2 to New Mexico"""

import sys
from model_state import Base, State

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = db.create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Sess = sessionmaker(bind=engine)
    session = Sess()
    result = session.query(State).get(2)

    result.name = 'New Mexico'

    session.commit()
