from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .engine import Base

class DocumentStat(Base):
    __tablename__ = "document_stats"
    id = Column(Integer, primary_key=True)
    term = Column(String, unique=True, index=True)
    doc_freq = Column(Integer, default=0)