#!/usr/bin/python3
"""Lists states with an 'a'"""

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
    result = session.query(State).all()
    char_match = set('a')

    for row in result:
        i = 0
        while i < len(row.name):
            if row.name[i] in char_match:
                print(f"{row.id}: {row.name}")
                break
            i += 1
