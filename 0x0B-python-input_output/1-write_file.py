#!/usr/bin/python3
""" Module contains function to write to file """


def write_file(filename="", text=""):
    """ Function to write to file """
    with open(filename, 'w', encoding="utf-8") as f:
        written_data = f.write(text)
    return written_data
