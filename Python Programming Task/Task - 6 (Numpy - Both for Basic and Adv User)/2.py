'''
You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

'''
import numpy
N = numpy.array(input().split(),int)
print(numpy.reshape(N,(3,3)))
