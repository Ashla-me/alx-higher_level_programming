#!/usr/bin/python3
"""module that defines append file function"""


def append_write(filename="", text=""):
    """it appends a text to a file

    Args:
        filename: file name to append to
        text: text to append"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
