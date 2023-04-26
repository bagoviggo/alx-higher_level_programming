#!/usr/bin/python3
"""Python Script that checks the last digit of a random number
    acknowledges if last digit is greater than 5, equal to 0, less than 6
"""
import random

number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
    print("Last digit of {} is {} and is ", end="".format(number, digit))
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
