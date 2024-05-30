#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """Tokenize and prints the text"""
    a = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in (':', '.', '?'):
            a = 1
            print(i)
        else:
            if a == 1 and i == " ":
                print()
            elif a == 1 and i != " ":
                print()
                print(i, end="")
            else:
                print(i, end="")
            a = 0
