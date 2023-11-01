#!/bin/bash

if [ "$FETCH_NOTEBOOKS" == "Yes" ] && [ ! -d "/docs/notebooks" ]
then
    git clone --depth 1 --branch stable \
        https://github.com/GeoscienceAustralia/dea-notebooks /docs/notebooks
fi

rm -r /output/*

sass /docs/_static/styles/index.scss /docs/_static/styles/styles.css

sphinx-build \
    -b dirhtml \
    -j auto \
    /docs /output

if [ "$DEMO_SERVER" == "Yes" ]
then
    cd /output
    python3 -m http.server 8011
fi
