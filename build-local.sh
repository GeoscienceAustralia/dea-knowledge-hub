#!/bin/bash

rm -r /output/*

sass --style=expanded /docs/_static/styles/index.scss /docs/_static/styles/styles.css

cp /docs/_robots/robots-local.txt /docs/robots.txt

sphinx-build -b dirhtml -j auto -a /docs /output

cd /output
python -m http.server 8011
