#!/bin/bash

if [ "$1" == "build_generator" ]; then
    docker build -t generator_image ./data_generator
elif [ "$1" == "run_generator" ]; then
    docker run --rm -v "$(pwd)/data:/data" generator_image
elif [ "$1" == "create_local_data" ]; then
    python ./data_generator/generate.py local_data
elif [ "$1" == "build_reporter" ]; then
    docker build -t analyser_image ./data_analyser
elif [ "$1" == "run_reporter" ]; then
    docker run --rm -v "$(pwd)/data:/data" analyser_image
fi