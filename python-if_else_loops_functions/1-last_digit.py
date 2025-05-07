#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    lastDig = (number % 10) * -1
    number *= -1
else:
    lastDig = number % 10
if lastDig > 5:
    print(f"Last digit of {number} is {lastDig} and is greater than 5")
elif lastDig == 0:
    print(f"Last digit of {number} is {lastDig} and is 0")
else:
    print(f"Last digit of {number} is {lastDig} and is less than 6 and not 0")
