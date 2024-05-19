#!/usr/bin/python3
def print_last_digit(number):
    temp = number
    if temp < 0:
        temp = temp * - 1
    last = temp % 10
    if number < 0:
        last = temp % 10 * -1
    print(last, end="")
    return last
