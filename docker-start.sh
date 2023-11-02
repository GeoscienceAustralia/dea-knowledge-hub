#!/bin/bash

rm -r /output/*

sass --style=compact /docs/_static/styles/index.scss /docs/_static/styles/styles.css

sphinx-build -b dirhtml -j auto /docs /output \
    | grep --invert-match --regexp "WARNING.*Document headings start at" \
    | grep --invert-match --regexp "WARNING.*duplicate label" \
    | grep --invert-match --regexp "WARNING: Pygments lexer name 'ipython3' is not known" \
    | grep --invert-match --regexp ".*GET /_.*"

if [ "$PRODUCTION_MODE" == "No" ]
then
    cd /output
    python3 -m http.server 8011
fi
