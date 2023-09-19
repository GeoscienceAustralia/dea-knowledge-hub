#!/bin/bash

if [ "$FETCH_NOTEBOOKS" == "Yes" ]
then
    git clone --depth 1 --branch stable \
        https://github.com/GeoscienceAustralia/dea-notebooks /docs/content/notebooks
fi

if [ "$BUILD_MODE" == "Development" ]
then
    sphinx-autobuild \
        --host 0.0.0.0 \
        --port 8011 \
        --ignore "/docs/content/tags/*" \
        -b dirhtml \
        -j auto \
        /docs/content /docs/_build/html
fi
