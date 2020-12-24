#!/usr/bin/env bash

die () { echo "$1" >&2; exit 1; }


hash aws || { die "Missing awscli. Exiting..."; }


stackName="my-stack"
if ! aws cloudformation deploy \
    --stack-name "my-stack" \
    --template-file ./deploy/cf-templates/app.yml \
    --parameter-overrides Environment="$ENVIRONMENT" \
    --no-fail-on-empty-changeset; then

    die "Failed to deploy $stackName stack"
fi
