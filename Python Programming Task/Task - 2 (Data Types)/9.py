'''

Given  sets of integers,  and , print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
Set1 = set(list(map(int,input().split())))
N = int(input())
Set2 = set(list(map(int,input().split())))
print(Set1.difference(Set2))
print(Set2.difference(Set1))
