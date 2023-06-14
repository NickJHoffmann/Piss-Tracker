#!/bin/bash

isort --line-length=90 .
yapf --in-place --recursive --style='{based_on_style: pep8, column_limit: 90, indent_width: 4, blank_line_before_nested_class_or_def: True, split_before_logical_operator: True, split_before_first_argument: True, split_penalty_import_names: 100}' .