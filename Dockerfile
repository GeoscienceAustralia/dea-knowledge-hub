FROM python:3.11

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y bash
RUN apt-get install -y pandoc
RUN apt-get install -y sass

WORKDIR /usr/src/app

RUN mkdir -p ./setup
RUN mkdir -p ./docs
RUN mkdir -p ./output

COPY docs/requirements.txt ./setup
RUN pip install -r ./setup/requirements.txt

COPY docs ./docs

COPY build-local.sh .
COPY Makefile .
CMD /bin/bash -c "./build-local.sh"

EXPOSE 8062
