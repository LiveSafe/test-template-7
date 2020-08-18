#!/bin/bash

# This script will configure your new lambda repository
# It is designed to be idempotent in case of typos, but
# is only intended to be run once after the repository
# has been cloned initially.

# TODO: set up this script to set up your repo for other types of lambda functions than just python

# verify script is being run from the correct directory
REPO_ROOT="$(git rev-parse --show-toplevel)"
CURRENT_DIR="$(pwd)"

if [ "${REPO_ROOT}" != "${CURRENT_DIR}" ]; then
    echo "Error, you are calling this command from the wrong directory, it should be run from the root of your repository."
    return
fi

repository_name="$(basename ${REPO_ROOT})"

# collect parameters for serverless.yml
read -p "Enter service name: [${repository_name}]: " service_name
service_name="${service_name:-${repository_name}}"
read -p "Enter default region: [us-west-2]: " default_region
default_region="${default_region:-us-west-2}"
read -p "Enter default environment: [develop]: " default_env
default_env="${default_env:-develop}"

echo "Updating serverless.yml..."
cat scripts/serverless.yml.template \
  | sed "s/SERVICE_NAME/${service_name}/g" \
  | sed "s/DEFAULT_REGION/${default_region}/g" \
  | sed "s/DEFAULT_ENVIRONMENT/${default_env}/g" > serverless.yml
echo "Repository configuration finished."
