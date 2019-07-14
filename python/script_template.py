#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Python version assertion may be required to warn incompatibility.
assert sys.version_info <= (3, 6), "Python version must be less that 3.6, not ported to 3.7 or higher."

from argparse import ArgumentParser
from collections import namedtuple


ArgsParsed = namedtuple("ArgsParsed", [])

def is_valid_foo(foo):
    """Foo is needed to start the magic."""
    if not foo:
        raise ValueError("Not foo in the bar.")

def validate_arguments(args):
    """Check arguments values if needed."""
    pass

def process_arguments():
    """Initialize the script arguments with validations."""
    parser = ArgumentParser(description="foo")
    # parser.add_argument()
    parsed_args = parser.parse_args()
    return ArgsParsed()

def main(args):
    """Magic start here with the arguments ready to go!"""
    pass


if __name__ == "__main__":
    args = process_arguments()
    main(args)
