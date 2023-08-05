FROM python:3.10-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY alembic/ app/alembic/
COPY alembic.ini app/

WORKDIR app

CMD ["alembic", "upgrade", "head"]

COPY src/ src/

WORKDIR src

CMD ["python", "main.py"]
