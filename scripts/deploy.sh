#!/usr/bin/env bash

set -exo pipefail

aws cloudformation deploy \
    --template build/template.yaml \
    --stack-name CustomResource-S3-Object-Demo-Stack \
    --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
    --parameter-overrides CreateObject="$CREATE_OBJECT" \
        ObjectKey="$OBJECT_KEY" \
        ObjectContent="$OBJECT_CONTENT"