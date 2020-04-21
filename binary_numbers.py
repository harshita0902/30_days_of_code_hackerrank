#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b = list(bin(n))
    b = b[2:]
    count=0
    maxx=0
    for i in range(len(b)):
        if b[i]=='1':
            count+=1
        else:
            if maxx<count:
                maxx=count
            count=0
    if maxx<count:
        print(count)
    else:
        print(maxx)
