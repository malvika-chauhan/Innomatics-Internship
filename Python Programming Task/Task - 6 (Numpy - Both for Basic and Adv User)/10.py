'''

You are given a 2-D array with dimensions X.
Your task is to perform the min function over axis  and then find the max of that.

'''
import numpy
N,M = input().split()
A = numpy.array([input().split() for _ in range(int(N))],int)
minn = numpy.min(A,axis=1)
print(numpy.max(minn))
