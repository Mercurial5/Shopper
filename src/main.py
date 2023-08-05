from models import session, Product
from utils import get_logger

logger = get_logger(__name__)


def main():
    session.add(Product(name='Test', description='Test product', price=1000))
    session.commit()

    for product in session.query(Product).all():
        print(product)  


if __name__ == '__main__':
    main()
