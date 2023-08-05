from uuid import uuid4

from sqlalchemy import Column, UUID, String, Text, Numeric

from models import DeclarativeBase


class Product(DeclarativeBase):
    __tablename__ = 'product'

    id = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), index=True)
