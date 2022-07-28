'''
You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.

'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    l= input().split()
    if l[0]=='pop':
       s.pop()
    elif l[0]=='remove':
       s.remove(int(l[1]))
    else:
        s.discard(int(l[1]))
print(sum(s))

