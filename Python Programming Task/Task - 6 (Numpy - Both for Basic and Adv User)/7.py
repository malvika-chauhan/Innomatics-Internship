'''

Task

You are given two integer arrays,  and  of dimensions X.
Your task is to perform the following operations:

Add ( + )
Subtract ( - )
Multiply ( * )
Integer Division ( / )
Mod ( % )
Power ( ** )

'''

import numpy
N,M = input().split()
A = numpy.array([input().split() for _ in range(int(N))],int)
B = numpy.array([input().split() for _ in range(int(N))],int)
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(A//B)
print(numpy.mod(A,B))
print(numpy.power(A,B))
