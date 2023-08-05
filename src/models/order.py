from uuid import uuid4

from sqlalchemy import Column, UUID, ForeignKey
from sqlalchemy.orm import relationship

from models import DeclarativeBase


class Order(DeclarativeBase):
    __tablename__ = 'order'

    id = Column(UUID, primary_key=True, default=uuid4)
    customer_id = Column(UUID, ForeignKey('customer.id'))

    customer = relationship('Customer', back_populates='orders')
