#!/bin/bash

FILES=$(find src -type f -name "*.py" -not -path "*/migrations/*")
pylint ${FILES}