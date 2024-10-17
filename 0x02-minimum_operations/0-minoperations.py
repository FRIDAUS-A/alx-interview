#!/usr/bin/env python3
"""
    write a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
        Args:
            n: number of H to have in the file
        Return:
            returns an integer that tells the min number
            of operatons to get the desired number of H
    """
    sum = 0
    i = 2
    while (n > 1):
        if n % i == 0:
            n = n / i
            sum += i
            i = 2
        else:
            i += 1
    return sum
