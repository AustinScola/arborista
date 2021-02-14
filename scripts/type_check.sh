#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ARBORISTA="$(realpath "${HERE}/..")"

cd "${ARBORISTA}"

source "${ARBORISTA}/scripts/library/venv.sh"
use_venv "test" frozen_test_requirements.txt

python3 -m mypy
