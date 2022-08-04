'''

You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.


'''

import numpy
N,M = numpy.array(input().split())
arr = numpy.array([input().split() for _ in range(int(N))],int)
print(numpy.transpose(arr))
print(arr.flatten())
