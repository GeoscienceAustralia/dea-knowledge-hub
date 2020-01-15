#!/bin/bash

# Travis-CI Needs an external script to run multiple deployment commands. :sadface:
#

pip install awscli
aws s3 sync --size-only --delete _build/html/ s3://docs.dea.ga.gov.au
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID --paths '/*'
