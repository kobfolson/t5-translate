#!/usr/bin/env sh

# create the directory
mkdir model-data \
    # download the files
    && wget https://huggingface.co/t5-base/raw/main/config.json -P ./model-data \
        && wget https://huggingface.co/t5-base/raw/main/tokenizer.json -P ./model-data \
            && wget https://huggingface.co/t5-base/resolve/main/pytorch_model.bin -P ./model-data