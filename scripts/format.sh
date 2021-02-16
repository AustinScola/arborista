#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
ARBORISTA="$(realpath "${HERE}/..")"

cd "${ARBORISTA}"

source "${ARBORISTA}/scripts/library/venv.sh"
use_venv "developer" frozen_developer_requirements.txt

source "${ARBORISTA}/scripts/library/cpus.sh"
NUMBER_OF_CPUS="$(get_number_of_cpus)"

python3 -m yapf --parallel -i -r .
python3 -m isort --jobs "${NUMBER_OF_CPUS}" .
