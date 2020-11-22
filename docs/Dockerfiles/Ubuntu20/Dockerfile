FROM ubuntu:20.04

WORKDIR /home/CC1-Conservatorio

RUN apt update \
  && apt -y upgrade \
  && apt install -y python3-pip

COPY hola.py ./

CMD python3 hola.py
