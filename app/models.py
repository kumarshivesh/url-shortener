from sqlalchemy import Column, String, Integer
from .database import Base

class URL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, unique=True, index=True)
    short_code = Column(String, unique=True, index=True)

