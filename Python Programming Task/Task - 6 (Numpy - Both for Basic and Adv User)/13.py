'''

You are given two arrays:  A and B.
Your task is to compute their inner and outer product.

'''
import numpy
A = numpy.array(input().split(),int)
B = numpy.array(input().split(),int)
print(numpy.inner(A,B))
print(numpy.outer(A,B))

