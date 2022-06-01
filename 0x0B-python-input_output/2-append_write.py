#!/usr/bin/python3
""" Module contains function to append to files """


def append_write(filename="", text=""):
    """ Function to append to file """
    with open(filename, 'a', encoding="utf-8") as f:
        written_data = f.write(text)
    return written_data
