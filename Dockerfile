# set base image (host OS)
FROM python:3.10-slim

ENV SERVICE=/home/app/service

RUN mkdir -p $SERVICE
RUN mkdir -p $SERVICE/static

# set the working directory in the container
WORKDIR $SERVICE

# Download latest listing of available packages:
RUN apt-get -y update

# Upgrade already installed packages:
RUN apt-get -y upgrade

# Install a new package:
RUN apt-get -y install libpq-dev
RUN apt-get -y install gcc

COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy the content of the local app directory to the working directory
COPY . .

# command to run on container start

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]