'''

Task

You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

'''

import numpy
N,M,P = input().split()
arr1 = numpy.array([input().split() for _ in range(int(N))],int)
arr2 = numpy.array([input().split() for _ in range(int(M))],int)
print(numpy.concatenate((arr1,arr2)))
