#!/usr/bin/env bash
pandoc --from=markdown --to=rst --output=README.rst README.md
/bin/rm -rf dist build
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
