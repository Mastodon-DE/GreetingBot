FROM python:3.12-alpine


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir mastodon.py

COPY main.py /usr/src/app/main.py
COPY register.py /usr/src/app/register.py

CMD python --version && python main.py