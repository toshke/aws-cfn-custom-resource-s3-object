#!/usr/bin/env bash

set -exo pipefail

aws cloudformation deploy \
    --template build/template.yaml \
    --stack-name CustomResource-S3-Object-Demo-Stack \
    --capabilities CAPABILITY_IAM