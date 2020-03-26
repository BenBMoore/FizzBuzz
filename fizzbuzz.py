"""
This is the "fizzbuzz" module.

The module supplies one function, fizzbuzz(). For example:
>>>fizzbuzz(15)
"FizzBuzz!"
"""


def fizzbuzz(x):
    assert int(x), "Must be a number"
    assert (x >= 0), 'Number must be greater than or equal to 0'

    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz!"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x
