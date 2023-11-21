#!/bin/bash

rm -r /output/*

sass --style=expanded /docs/_static/styles/index.scss /docs/_static/styles/styles.css

cp /docs/_robots/robots-dev.txt /docs/robots.txt

sphinx-build -b dirhtml -j auto /docs /output

cd /output
python -m http.server 8011
