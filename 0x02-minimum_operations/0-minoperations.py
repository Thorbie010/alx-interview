#!/usr/bin/python3
""" Script for Minimum Operations """


def minOperations(n):
    """ Function for Minimum Operations.
    Returns an integer.
    If n is impossible to achieve, return 0 """

    if n <= 1:
        return 0

    x = 0
    y = 2

    while n > 1:
        while n % y == 0:
            x += y
            n //= y
        y += 1

    return x
