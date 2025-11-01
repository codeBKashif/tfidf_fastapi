from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .engine import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    terms = relationship("TermStat", back_populates="document", cascade="all, delete")