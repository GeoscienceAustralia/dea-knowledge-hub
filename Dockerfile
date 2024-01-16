FROM python:3.11

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y bash
RUN apt-get install -y pandoc
RUN apt-get install -y sass

RUN mkdir -p /setup
RUN mkdir -p /docs
RUN mkdir -p /output

COPY requirements.txt /setup
RUN pip install -r /setup/requirements.txt

COPY docs /docs

COPY build-local.sh /setup
CMD /bin/bash -c "/setup/build-local.sh"

EXPOSE 8062
