'''
Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example
n=3
The list of non-negative integers that are less than n=3 is{0,1,2} . Print the square of each number on a separate line.
'''
if __name__ == '__main__':
    n = int(raw_input())
    if(n>=1 and n<=20):
        for i in range(n):
            print(i*i)

