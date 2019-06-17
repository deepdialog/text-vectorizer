#!/bin/bash

set -e
flake8 ./text_vectorizer/*.py
flake8 ./text_vectorizer/**/*.py
pydocstyle text_vectorizer
