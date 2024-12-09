import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))

def calc(a, b):
    return math.sqrt(a**2 + b**2)

hypotenuse = calc(a, b)
print("Hypotenuse=",hypotenuse)


import random

a = float(input("Enter a: "))
b = float(input("Enter b: "))

random_number = random.uniform(a, b)
print("Random number between", a, "and", b, "is:", random_number)
