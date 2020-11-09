#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ARBORISTA="$(realpath "${HERE}/..")"

pushd "${ARBORISTA}" > /dev/null
trap "popd > /dev/null" EXIT

python3 -m pylint arborista tests
