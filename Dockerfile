FROM python:3.10-slim

COPY . /app
WORKDIR /app/

RUN apt-get update
RUN apt install --fix-broken -y
RUN apt-get install build-essential libssl-dev libffi-dev python-dev -y
RUN pip install -r requirements.txt

CMD python run.py