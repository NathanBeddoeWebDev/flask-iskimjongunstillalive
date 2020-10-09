FROM python:3

MAINTAINER Nathan Beddoe "nbedd2@protonmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev cron

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

RUN /bin/bash -c "mv /executeJob.sh /etc/cron.hourly/executeJob.sh"

CMD [ "main.py" ]