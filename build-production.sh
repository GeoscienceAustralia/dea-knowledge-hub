#!/bin/bash

python -m pip install --upgrade pip
python -m pip install -r ./requirements.txt

npm install -g sass

apt-get install -y pandoc

mkdir -p ./output

sass --style=compressed ./docs/_static/styles/index.scss ./docs/_static/styles/styles.css

cp ./docs/_robots/robots-production.txt ./docs/robots.txt

sphinx-build -b dirhtml -j auto ./docs ./output
