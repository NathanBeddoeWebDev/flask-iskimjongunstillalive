FROM ubuntu:18.04

MAINTAINER Nathan Beddoe "nbedd2@protonmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]