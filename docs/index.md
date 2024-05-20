# pycodecov

[![CI](https://github.com/kiraware/pycodecov/workflows/ci/badge.svg)](https://github.com/kiraware/pycodecov/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kiraware/pycodecov/workflows/codeql/badge.svg)](https://github.com/kiraware/pycodecov/actions/workflows/codeql.yml)
[![Docs](https://readthedocs.org/projects/pycodecov/badge/?version=latest)](https://pycodecov.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/kiraware/pycodecov/graph/badge.svg?token=R7FIQXO4UP)](https://codecov.io/gh/kiraware/pycodecov)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pypi](https://img.shields.io/pypi/v/pycodecov.svg)](https://pypi.org/project/pycodecov/)
[![python](https://img.shields.io/pypi/pyversions/pycodecov.svg)](https://pypi.org/project/pycodecov/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/license/mit/)

This is documentation for the `pycodecov` project that
is an asynchronous api wrapper written in Python for
[open data](https://data.pycodecov.go.id/) on weather
forecasts and latest earthquakes in Indonesia served
by Meteorology, Climatology and Geophysics Agency
([Codecov](https://pycodecov.go.id/)).

pycodecov was created as a wrapper to handle API requests
Codecov open data asynchronously. This is because the
available API does not follow API standards in general,
therefore a wrapper was created which is expected to
make it easier to use the Codecov open data API with Python.

We use the third party library [aiohttp](https://docs.aiohttp.org/en/stable/)
for asynchronous client requests and it has been tested
to work well using the [asyncio](https://docs.python.org/3/library/asyncio.html)
library. Also it use [dataclass](https://docs.python.org/3/library/dataclasses.html)
as the schema.

## Table Of Contents

You can start reading the documentation with the
following links:

1. [Tutorials](tutorials.md)
2. [How-To Guides](how-to-guides.md)
3. [Reference](reference/api.md)

## Acknowledgements

We would like to thank the Meteorology, Climatology
and Geophysics Agency (Codecov) for its [open data service](https://data.pycodecov.go.id/)
on weather forecasts and latest earthquake information.
