'''

You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.

'''

import numpy
P = numpy.array((input().split()) ,float)
x = input()
print(numpy.polyval(P,int(x)))

