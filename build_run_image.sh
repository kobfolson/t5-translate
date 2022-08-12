#!/usr/bin/env sh

docker build . -t t5-translate \
    && docker run --name t5-translator -e URL_PREFIX=/api/v1 -p 8080:8080 t5-translate