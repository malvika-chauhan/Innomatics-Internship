'''

You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

'''

import numpy
N = tuple(map(int,input().split()))
print(numpy.zeros(N, dtype = numpy.int))
print(numpy.ones(N, dtype = numpy.int))
