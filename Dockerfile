FROM python:3.10-slim as base
RUN apt-get update
RUN apt-get install build-essential libssl-dev libffi-dev python-dev -y

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Now multistage build
FROM python:3.10-slim
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED 1
CMD python run.py
