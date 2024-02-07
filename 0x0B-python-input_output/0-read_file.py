#!/usr/bin/python3
"""
a function that reads a text file
"""

def read_file(filename=""):
    """it prints the content of a UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as rf:
        read_file = rf.read()
        print(read_file, end="")
