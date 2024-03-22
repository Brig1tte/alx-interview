#!/usr/bin/python3
"""
This bash script module finds the minimum operations to duplicate
a letter in a file
"""


def minOperations(n: int) -> int:
    """ Funct to calculate fewer numb of opreations required to
    result in exactly "n" "H" characters

    Return:
        The minimum number of operations possible
    """
    operations: int = 0
    divisor: int = 2

    if n <= 1:
        return 0
    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n /= divisor
        else:
            divisor += 1

    return operations
