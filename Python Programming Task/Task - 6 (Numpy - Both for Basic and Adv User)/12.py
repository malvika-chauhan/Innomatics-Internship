'''

You are given two arrays A and B. Both have dimensions of NXN.
Your task is to compute their matrix product.



'''
import numpy
N = input()
Array1 = numpy.array([input().split() for _ in range(int(N))],int)
Array2 = numpy.array([input().split() for _ in range(int(N))],int)
print(numpy.dot(Array1,Array2))

