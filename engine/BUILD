load("@rules_python//python:defs.bzl", "py_binary")

package(default_visibility = ["//visibility:public"])

py_binary(
  name = "engine",
  main = "translator.py",
  srcs = glob(["*.py"]),
  python_version = 'PY3',
)
