FROM python:3.12-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt .
COPY main.py /usr/src/app/main.py

RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py