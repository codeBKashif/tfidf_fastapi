from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .engine import Base

class TermStat(Base):
    __tablename__ = "term_stats"
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    term = Column(String, index=True)
    tf = Column(Float)
    document = relationship("Document", back_populates="terms")