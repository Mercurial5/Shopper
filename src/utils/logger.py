import logging

logging_format = {
    'name': '%(name)s',
    'level': '%(levelname)s',
    'msg': '%(message)s'
}
logging_format = str(logging_format)

date_format = "%Y-%m-%dT%H:%M:%S %Z"
logging.basicConfig(level=logging.INFO, format=logging_format, datefmt=date_format)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
