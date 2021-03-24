#!/usr/bin/env python

# This example has been taken from
# https://realpython.com/primer-on-python-decorators/#simple-decorators

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee! asdasd")


# say_whee = my_decorator(say_whee)


say_whee()
