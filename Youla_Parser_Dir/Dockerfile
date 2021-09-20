FROM python:latest

RUN mkdir -p /usr/app/

WORKDIR /usr/app/

COPY . /usr/app/

RUN pip3 install poetry
RUN poetry install


CMD ["python3", "main.py"]