#!/bin/bash

set -eox pipefail

python -m pip install --upgrade pip
python -m pip install -r ./docs/requirements.txt

npm install -g sass

sudo apt-get install -y pandoc
