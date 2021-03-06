#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Case for positive numbers
if number > 0:
    positiveDigit = number % 10
    if positiveDigit > 5:
        firstPart = "Last digit of " + str(number) + " is "
        secondPart = str(positiveDigit) + " and is greater than 5"
        print(firstPart + secondPart)

    if (positiveDigit < 6) & (positiveDigit != 0):
        firstPart = "Last digit of " + str(number) + " is "
        secondPart = str(positiveDigit) + " and is less than 6 and not 0"
        print(firstPart + secondPart)

# Case for negative numbers: Converting the last number into a positive
if number < 0:
    negativeDigit = number % -10
    if negativeDigit > 5:
        firstPart = "Last digit of " + str(number) + " is "
        secondPart = str(negativeDigit) + " and is greater than 5"
        print(firstPart + secondPart)

    if (negativeDigit < 6) & (negativeDigit != 0):
        firstPart = "Last digit of " + str(number) + " is "
        secondPart = str(negativeDigit) + " and is less than 6 and not 0"
        print(firstPart + secondPart)

# Case for zero
if number == 0:
    print("Last digit of " + str(number) + " is " + str(number) + " and is 0")
