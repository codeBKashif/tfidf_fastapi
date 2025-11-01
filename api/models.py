from sqlalchemy import (
    create_engine, Column, Integer, String, Float, ForeignKey
)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from contextlib import contextmanager


engine = create_engine("sqlite:///tfidf.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()



class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    terms = relationship("TermStat", back_populates="document", cascade="all, delete")

class TermStat(Base):
    __tablename__ = "term_stats"
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    term = Column(String, index=True)
    tf = Column(Float)
    document = relationship("Document", back_populates="terms")

class DocumentStat(Base):
    __tablename__ = "document_stats"
    id = Column(Integer, primary_key=True)
    term = Column(String, unique=True, index=True)
    doc_freq = Column(Integer, default=0)


def create_tables():
    Base.metadata.create_all(engine)

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()    