#!/usr/bin/python3
"""lookup module"""

def lookup(obj):
    """lookup method
    returns a list of available attributes and methods
    of an object"""
    return dir(obj)
