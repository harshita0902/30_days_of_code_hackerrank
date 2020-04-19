#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    fact=1
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == '__main__':
    n = int(input())

    result = factorial(n)
    print(result)
