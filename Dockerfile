FROM python:3.10-slim

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

RUN chmod +x /app/bin/*
ENV PATH "$PATH:/app/bin"

CMD start
