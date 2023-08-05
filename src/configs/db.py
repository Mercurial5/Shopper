from os import environ

from sqlalchemy import URL


class DBConfig:
    DRIVER_NAME = environ['DB_DRIVER_NAME']
    USERNAME = environ['DB_USERNAME']
    PASSWORD = environ['DB_PASSWORD']
    DATABASE = environ['DB_DATABASE']
    HOST = environ['DB_HOST']
    PORT = int(environ['DB_PORT'])

    @classmethod
    def get_engine_url(cls) -> URL:
        return URL.create(drivername=cls.DRIVER_NAME, username=cls.USERNAME, password=cls.PASSWORD,
                          database=cls.DATABASE, host=cls.HOST, port=cls.PORT)
