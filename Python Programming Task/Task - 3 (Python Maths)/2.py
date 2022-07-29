'''
Your task is to find  (angle , as shown in the figure) in degrees.

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a = int(input())
b = int(input())
M = math.sqrt(a**2+b**2)
theta = math.acos(b/M )
print(str(round(math.degrees(theta)))+'\xb0')
