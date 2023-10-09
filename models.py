from database import Base
from sqlalchemy import Column, Integer, String


class NextEventTruncated(Base):
    __tablename__ = "next_event_truncated"
    index = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    location = Column(String)
    red_fighter = Column(String)
    blue_fighter = Column(String)
    red_record = Column(String)
    blue_record = Column(String)
