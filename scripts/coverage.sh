#!/bin/bash

set -e

coverage erase
coverage run -a --source=. -m tests
coverage report -m