'''
You are given a 1-D array, . Your task is to print the ,  and  of all the elements of .


'''

import numpy
numpy.set_printoptions(legacy='1.13')
A = numpy.array(input().split(),float)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
