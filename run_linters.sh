#!/usr/bin/env sh

isort . && black . && flake8 .\
    && mypy \
        --ignore-missing-imports \
        --follow-imports=skip \
        --strict-optional .
