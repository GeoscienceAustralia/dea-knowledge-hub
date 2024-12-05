#!/bin/bash

set -eox pipefail

mkdir -p ./output

sass --style=compressed ./docs/_static/styles/index.scss ./docs/_static/styles/styles.css

cp ./docs/_robots/robots-demo.txt ./docs/robots.txt

make build
