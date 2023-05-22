FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl python3.10 python3-pip python3.10-venv python-is-python3
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install nodejs

RUN npm install ganache --global

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt
