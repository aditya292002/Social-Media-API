
# In this file we will create our database/sqlalchemy models

from .database import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from datetime import datetime

class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)




