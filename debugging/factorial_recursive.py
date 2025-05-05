#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.
                 n! represents the product of all positive integers less than
                 or equal to n.
    
    Returns:
        int: The factorial of n (n!).
             For n = 0, returns 1 (0! = 1 by definition).
             For n > 0, returns the product of all integers from 1 to n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
