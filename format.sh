#!/bin/bash

find . -name "*.py" | xargs python3 -m yapf -i

find . -name "*.py" | xargs python3 -m isort -i
