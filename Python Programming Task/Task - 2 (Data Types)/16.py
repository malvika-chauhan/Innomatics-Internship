'''
You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

Your task is to execute those operations and print the sum of elements from set .

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
A1 = set(map(int,input().split()))
N = int(input())
for i  in range(0,N):
   a = list(map(str,input().split()))
   B1 = set(map(int,input().split()))
   if(a[0]=='update'):
    A1.update(B1)
   elif(a[0]=='intersection_update'):
    A1.intersection_update(B1)
   elif(a[0]=='difference_update'):
    A1.difference_update(B1)
   else:
    A1.symmetric_difference_update(B1)
print(sum(A1))
