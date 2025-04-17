from sqlalchemy import Column, Integer, String, Boolean
from ..db.db import Base

class Part(Base):
    __tablename__ = "part"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    sku = Column(String(30))
    description = Column(String(1024))
    weight_ounces = Column(Integer)
    is_active = Column(Boolean)
