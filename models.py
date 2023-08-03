from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ransomware(Base):
    __tablename__ = 'ransomware'

    id = Column(Integer, primary_key=True)
    group = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
