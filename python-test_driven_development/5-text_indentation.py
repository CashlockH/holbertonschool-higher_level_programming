#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """Tokenize and prints the text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace("  ", "").replace(": ", ":")
    text = text.replace("? ", "?").replace(". ", ".")
    for i in text:
        print(i, end="")
        if i in (':', '?', '.'):
            print('\n')
