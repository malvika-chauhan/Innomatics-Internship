'''
You are given a complex . Your task is to convert it to polar coordinates.

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
print(*cmath.polar(complex(input())),sep='\n')
