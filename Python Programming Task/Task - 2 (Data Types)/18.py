'''
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set A is subset of set B, print True.
If set A is not a subset of set B , print False

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    A = int(input())
    set1 = set(map(int,input().split()))
    B = int(input())
    set2 = set(map(int,input().split()))   
    print(set1==set2.intersection(set1))
