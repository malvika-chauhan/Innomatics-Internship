'''

You are given a square matrix A with dimensions NXN. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

'''

import numpy
N = input()
A = numpy.array([input().split() for _ in range(int(N))],float)
print(round(numpy.linalg.det(A),2))

