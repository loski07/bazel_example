# bazel_example

## Introduction
This project is an attempt to build, test and run [a Python project](https://github.com/loski07/aid_template_engine) using Bazel.

## Requirements
- Bazel
- Python3

## Execution
- Build: `bazel build //engine:engine`
- Test: `bazel test //tests/engineTests:engine_test`. It does not work, it should fail.
- Run: `bazel run //engine:engine`
- Clean: `bazel clean`
