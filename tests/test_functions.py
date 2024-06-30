#!/usr/bin/env python3

"""
Module of unit test
"""

from Testing_project import functions

def test_add():
    assert functions.add(5, 2) == 7.0


def test_add_type():
    ret = functions.add(5, 2)
    assert isinstance(ret, float)


def test_subtract():
    assert functions.subtract(19, 10) == 9.0


def test_subtract_type():
    ret = functions.subtract(19, 10)
    assert isinstance(ret, float)
