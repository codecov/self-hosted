#!/bin/bash
set -eu

NEW_VERSION="$1"

sed -i -e "s/^\# Self-Hosted Codecov .*/# Self-Hosted Codecov $NEW_VERSION/" README.md

echo "New version: $NEW_VERSION"
