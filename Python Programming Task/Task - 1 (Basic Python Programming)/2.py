'''
Task
Given an integer n , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  2 to 5, print Not Weird
If  is even and in the inclusive range of  6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, n.

Constraints
1<=n<=100

Print Weird if the number is weird. Otherwise, print Not Weird.
'''

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if(n>=1 and n<=100):
        if (n%2!=0):
            print("Weird")
        elif (n%2==0):
            if(n>=2 and n<=5):
                print("Not Weird")
            elif (n>=6 and n<=20):
                print("Weird")
            elif n>20:
                print("Not Weird")
