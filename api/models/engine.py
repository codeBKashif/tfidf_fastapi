from sqlalchemy import (
    create_engine
)
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager


engine = create_engine("sqlite:///tfidf.db")

Session = sessionmaker(bind=engine)

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(engine)

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()    