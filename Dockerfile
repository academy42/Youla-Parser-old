FROM python:3.9 as builder
ARG DATA_FILE

RUN mkdir src
WORKDIR /src
COPY . /src

ENTRYPOINT ['python', "main.py"]

CMD [ "python", "./main.py" ]