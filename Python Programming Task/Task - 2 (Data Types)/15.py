'''
Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
A = set(map(int,input().split()))
m= int(input())
B = set(map(int,input().split()))
print(len(A.symmetric_difference(B)))
