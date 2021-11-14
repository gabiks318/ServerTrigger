FROM python:alpine3.14

RUN ["mkdir", "/app"]
WORKDIR /app
COPY requirements.txt /app
RUN ["pip", "install", "-r", "/app/requirements.txt"]

COPY . /app

CMD ["python", "main.py"]