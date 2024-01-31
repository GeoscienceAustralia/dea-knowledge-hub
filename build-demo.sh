#!/bin/bash

python -m pip install -r ./requirements.txt

npm install -g sass

apt-get install -y pandoc

mkdir -p ./output

sass --style=compressed ./docs/_static/styles/index.scss ./docs/_static/styles/styles.css

cp ./docs/_robots/robots-demo.txt ./docs/robots.txt

sphinx-build -b dirhtml -j auto -a ./docs ./output
