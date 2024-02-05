#!/usr/bin/python3
"""
the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """ returns True if the object is a subclass of a_class"""
    return(issubclass(type(obj), a_class))
