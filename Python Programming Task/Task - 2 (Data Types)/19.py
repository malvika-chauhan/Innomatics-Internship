'''
ou are given a set  and  other sets.
Your job is to find whether set A  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())
c=0
for i in range(n):
    B = set(map(int,input().split()))
    if(B.difference(A)!=0) or str((len(A))==str(len(B))):
        c=1
if(c==1):
    print('False')
else:
    print('True')
    
