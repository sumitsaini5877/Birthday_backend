from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    caption = Column(Text)
    image_url = Column(Text)