[![Python application test with Github Actions](https://github.com/mlops-mx/codespace_test/actions/workflows/testing_ci.yml/badge.svg)](https://github.com/mlops-mx/codespace_test/actions/workflows/testing_ci.yml)

This repository is for testing github actions automation.

codespace_test/.github/workflows/testing_ci.yml

name: Python application test with Github Actions

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    ...
