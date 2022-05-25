#!/usr/bin/python3
""" Module that indents a text based on special characters """


def text_indentation(text):
    """Function that prints indented text and an extra newline
        Raises TypeError if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    special_chars = (".", "?", ":")

    for i in special_chars:
        text = text.replace(i, i + '\n')
    text = text.replace('\n ', '\n')
    text = text.replace(' \n', '\n')
    text = text.replace('\n', '\n\n')
    print(text, end="")
