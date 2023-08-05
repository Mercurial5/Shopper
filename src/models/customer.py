from sqlalchemy import Column, UUID
from sqlalchemy.orm import relationship

from models import DeclarativeBase


class Customer(DeclarativeBase):
    __tablename__ = 'customer'

    id = Column(UUID, primary_key=True)

    orders = relationship('Order', back_populates='customer')
