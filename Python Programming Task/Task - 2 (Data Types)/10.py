'''
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
arr = []
for i in range(N):
    arr.append(input())
print(len(set(arr)))

#print(len(set([str(input()) for i in range(N)])))

