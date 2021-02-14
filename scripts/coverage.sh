#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ARBORISTA="$(realpath "${HERE}/..")"

pushd "${ARBORISTA}" > /dev/null
trap "popd > /dev/null" EXIT

source "${ARBORISTA}/scripts/library/venv.sh"
use_venv "test" frozen_test_requirements.txt

python3 -m pytest --cov=arborista --cov-report term-missing
