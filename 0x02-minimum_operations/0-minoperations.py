#!/usr/bin/python3
"""
Bash script to execute only two operations: Copy All and Paste.
If n is impossible to achieve, return 0 else return an Integer.
"""


def minOperations(n: int) -> int:
    """ Funct to calculate the least number of opreations needed to
    result in exactly "n" "H" characters """

    operations: int = 0
    divs: int = 2

    if n <= 1:
        return 0
    while n > 1:
        if n % divs == 0:
            operations += divs
            n /= divs
        else:
            divs += 1

    return operations
