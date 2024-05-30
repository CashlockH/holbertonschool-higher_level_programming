#!/usr/bin/python3
def text_indentation(text):
    a = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in (':', '.', '?'):
            a = 1
            print(i)
        else:
            if a != 1:
                print(i, end="")
            else:
                print()
            a = 0
