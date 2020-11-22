FROM fedora:latest

WORKDIR /home/CC1-Conservatorio

RUN dnf install -y python3-setuptools python3-devel redhat-rpm-config

COPY hola.py ./

CMD python3 hola.py
