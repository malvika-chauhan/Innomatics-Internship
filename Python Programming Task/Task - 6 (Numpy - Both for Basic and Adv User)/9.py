'''
You are given a 2-D array with dimensions X.
Your task is to perform the sum tool over axis 0 and then find the product of that result

'''
import numpy
N,M = input().split()
A = numpy.array([input().split() for _ in range(int(N))],int)
prodd = numpy.sum(A,axis=0)
print(numpy.prod(prodd))
