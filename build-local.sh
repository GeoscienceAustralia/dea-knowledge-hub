#!/bin/bash

rm -r /output/*

if [ "$BUILD_MODE" == "production" ]
then
    sass --style=compressed /docs/_static/styles/index.scss /docs/_static/styles/styles.css
else
    sass --style=expanded /docs/_static/styles/index.scss /docs/_static/styles/styles.css
fi

if [ "$BUILD_MODE" == "production" ]
then
    cp /docs/_robots/robots-prod.txt /docs/robots.txt
else
    cp /docs/_robots/robots-dev.txt /docs/robots.txt
fi

sphinx-build -b dirhtml -j auto /docs /output

cd /output
python -m http.server 8011
