#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple module of example functions
"""

from typing import Union, Optional

def add(x: Union[int, float], y: Union[int, float]) -> float:
    """
    a function to add two numbers
    args:
        x int or float to add to y
        y int or float to add to x

    return:
        float sum of x and y
    """

    return float(x + y)


def subtract(x: Union[int, float], y: Union[int, float]) -> float:
    """
    a function to subtract two numbers
    args:
        x int or float to add to y
        y int or float to add to x

    return:
        float differnce of x and y

    doctest:
    >>> subtract(10, 9)
    1.0
    """

    return float(x - y)
