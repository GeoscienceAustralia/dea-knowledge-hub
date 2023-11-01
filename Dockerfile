FROM python:3.11

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y bash
RUN apt-get install -y pandoc
RUN apt-get install -y sass

RUN mkdir -p /setup
RUN mkdir -p /docs
RUN mkdir -p /output

COPY docker-start.sh /setup
COPY requirements.txt /setup
COPY docs /docs
RUN pip install -r /setup/requirements.txt

EXPOSE 8011

CMD /bin/bash -c "/setup/docker-start.sh"
