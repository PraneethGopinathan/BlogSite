FROM python:3.10-slim


COPY . /app
WORKDIR /app/

RUN mkdir .pip-cache
RUN apt-get update
RUN apt install --fix-broken -y
RUN apt-get install build-essential libssl-dev libffi-dev python-dev -y
RUN pip --cache-dir=.pip-cache install -r requirements.txt


# ENTRYPOINT [ "python" ]
# CMD [ "run.py" ]

CMD python run.py

EXPOSE 5000