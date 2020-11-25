#!/bin/bash

# Deploy the docs to S3 and invalidate the cloudfront distribution
#

pip install awscli
aws s3 sync --size-only --delete _build/html/ s3://docs.dea.ga.gov.au
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID --paths '/*'
