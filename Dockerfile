FROM python:3.11-alpine

RUN apk update
RUN apk add git
RUN apk add bash
RUN apk add pandoc
RUN apk add nodejs npm

RUN npm install -g sass
RUN npm install -g @mermaid-js/mermaid-cli

RUN mkdir -p /setup
RUN mkdir -p /docs
RUN mkdir -p /output

COPY docs/requirements.txt /setup
RUN pip install -r /setup/requirements.txt

COPY docs /docs

COPY build-local.sh /setup
CMD /bin/bash -c "/setup/build-local.sh"

EXPOSE 8062
