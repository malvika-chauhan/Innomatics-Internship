'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

'''


if __name__ == '__main__':
    N = int(input())
    listt=[]
    convo=[]

    for i in range(N):
        c = input().split()
        listt.append(c)
    for i in range(len(listt)):
        if listt[i][0] == 'insert':
            x = int(listt[i][1])
            y = int(listt[i][2])
            convo.insert(x,y)
        elif listt[i][0] == 'print':
            print(convo)
        elif listt[i][0] == 'remove':
            x = listt[i][1]
            convo.remove(int(x))
        elif listt[i][0] == 'append':
            x = listt[i][1]
            convo.append(int(x))
        elif listt[i][0] == 'sort':
            convo.sort()
        elif listt[i][0] == 'pop':
            convo.pop()
        elif listt[i][0] == 'reverse':
            convo.reverse()
