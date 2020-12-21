#!/usr/bin/env bash
set -exo pipefail
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
BUCKET_NAME="s3-object-custom-resource-demo-sources-$ACCOUNT_ID"
set +e
aws s3 mb s3://$BUCKET_NAME
set -e
rm -rf build/*
mkdir -p build
zip build/src.zip *.py
sam package -t template.cfn.yaml --s3-bucket $BUCKET_NAME --s3-prefix $DEPLOYMENT_PREFIX > build/template.yaml