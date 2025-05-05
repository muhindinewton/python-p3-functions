#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    pass
    print(f"Hello, {name}!")

greet("Naureen")

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    pass
    return num1 + num2

sum = add(45, 55)
print(sum)

def halve(number):
    pass
    return number/2
half_int = halve(100)

print (half_int)