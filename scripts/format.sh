#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ARBORISTA="$(realpath "${HERE}/..")"

pushd "${ARBORISTA}" > /dev/null
trap "popd > /dev/null" EXIT

source "${ARBORISTA}/scripts/library/venv.sh"
use_venv "developer" frozen_developer_requirements.txt

python3 -m yapf -i -r .
python3 -m isort .
