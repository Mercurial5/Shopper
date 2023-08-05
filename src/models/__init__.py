from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

from configs import DBConfig

engine = create_engine(DBConfig.get_engine_url())
DeclarativeBase = declarative_base()

session = Session(engine)

from models.order import Order
from models.product import Product
from models.customer import Customer
