FROM python:3.6

COPY . /app/
WORKDIR /app/app

RUN pip install -r req.txt
EXPOSE 5000
