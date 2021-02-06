FROM python:3.9.1-alpine

RUN apk update && apk add gcc musl-dev

COPY . /immosoup
WORKDIR /immosoup

RUN pip3 install --user bs4 telepot requests

ENTRYPOINT python3 main.py $ACCESS_TOKEN
