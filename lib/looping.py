#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        if i == 1:
            print(f"{i}")
            print("Happy New Year!")
            i -= 1
        else:
            print(f"{i}")
            i -= 1

def square_integers(int_list):
    squared_list = [integer * integer for integer in int_list]
    return squared_list

def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 15 == 0:
            print("FizzBuzz")
            i += 1
        elif i % 5 == 0:
            print("Buzz")
            i += 1
        elif i % 3 == 0:
            print("Fizz")
            i += 1
        else:
            print(f"{i}")
            i += 1
