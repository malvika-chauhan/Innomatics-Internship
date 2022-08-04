'''
Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.

'''

import numpy
numpy.set_printoptions(legacy='1.13')
N,M = input().split()
print(numpy.eye(int(N),int(M)))

