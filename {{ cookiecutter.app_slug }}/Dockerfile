FROM python:3.6

RUN apt-get update && apt-get install nginx -y && rm -rf /var/lib/apt/lists/*

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

ENV PATH="./:${PATH}"

EXPOSE 8080:8080
