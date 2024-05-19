#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
if temp < 0:
    temp = temp * -1
last = temp % 10
print(f"Last digit of {number} is {last} and", end=" ")
if last > 5:
    print("greater than 5")
elif last == 0:
    print("is 0")
else:
    print("less than 6 and not 0 ")
