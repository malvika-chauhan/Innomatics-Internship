'''

Task

You are given a 2-D array of size NXM.
Your task is to find:

The mean along axis 1
The var along axis 0
The std along axis none

'''

import numpy
M,N = map(int,input().split())
my_array = numpy.array([input().split() for i in range(N)],int)
print(my_array.mean(axis=1))
print(my_array.var(axis=0))
print(round((my_array.std()),11))
