#!/bin/bash

# Deploy the docs to S3 and invalidate the Cloudfront distribution

python -m pip install awscli
aws s3 sync --delete output s3://docs.dea.ga.gov.au
aws cloudfront create-invalidation --distribution-id $DISTRIBUTION_ID --paths '/*'
