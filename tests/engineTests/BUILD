load("@rules_python//python:defs.bzl", "py_test")

package(default_visibility = ["//visibility:private"])

py_test(
    name = "engine_test",
    srcs = glob(["*.py"]),
    main = "suite.py",
    deps = ["//engine:engine"],
)
