#!/bin/bash
set -eu

NEW_VERSION="$1"

sed -i -e "s/^\# Self-Hosted Codecov .*/# Self-Hosted Codecov $NEW_VERSION/" README.md
sed -i -e "s/\(Change Date:\s*\)[-0-9]\+\$/\\1$(date +'%Y-%m-%d')/" LICENSE

echo "New version: $NEW_VERSION"