FROM python:3.7

RUN mkdir -p /usr/app/

WORKDIR /usr/app/

COPY . /usr/app/

RUN pip install poetry
RUN poetry install



CMD ["python3", "./main.py"]