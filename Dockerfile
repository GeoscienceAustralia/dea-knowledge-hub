FROM python:3.11-alpine

RUN apk update
RUN apk add git
RUN apk add bash
RUN apk add pandoc

RUN mkdir -p /docs/scripts
RUN mkdir -p /docs/content
RUN mkdir -p /docs/_build

COPY requirements.txt /docs
COPY scripts /docs/scripts
RUN python3 -m pip install -r /docs/requirements.txt

EXPOSE 8011

CMD /bin/bash -c "/docs/scripts/docker-start.sh"
