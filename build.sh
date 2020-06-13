#!/usr/bin/env bash
set -e

echo "### TESTING ###"
python3 -m unittest discover -s tests

if [ "$1" == "publish" ]; then
  rm dist/*
  echo "### BUILDING WHEEL ###"
  python3 setup.py sdist
  echo "### PUBLISHING ###"
  python3 -m twine upload dist/*
fi
