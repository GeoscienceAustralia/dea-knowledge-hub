#!/bin/bash

rm -r /output/*

sass --style=compact /docs/_static/styles/index.scss /docs/_static/styles/styles.css

sphinx-build -b dirhtml -j auto /docs /output

if [ "$PRODUCTION_MODE" == "No" ]
then
    cd /output
    python3 -m http.server 8011
fi
