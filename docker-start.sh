#!/bin/bash

if [ "$FETCH_NOTEBOOKS" == "Yes" ] && [ ! -d "/docs/notebooks" ]
then
    git clone --depth 1 --branch stable \
        https://github.com/GeoscienceAustralia/dea-notebooks /docs/notebooks
fi

sass /docs/_static/styles/test.scss /output/test.scss

sphinx-build \
    -b dirhtml \
    -j auto \
    /docs /output
