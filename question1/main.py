"""
Question 1:
Write a Python function named generate_pyramid that takes two parameters:
1.
n (an integer): The number of levels in the pyramid.
2. char (a string, defaulting to '*'): The character to use for constructing the
pyramid.
The function should return a string representing a pyramid pattern of n levels using the
specified character. Each level of the pyramid should be centered, with the top level having
one character and each subsequent level having two more characters than the previous
one. Each level should be followed by a newline character (\n).
"""


def generate_pyramid(n, char):
    res = ""

    if n < 1:
        return res

    for i in range(n):
        res += " "*(n-i-1) + char*(2*i+1) + "\n"

    return res
