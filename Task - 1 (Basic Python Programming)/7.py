'''
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:
1234....n

Note that "" represents the consecutive values in between.

Example
n=5
Print the string . 12345
'''
if __name__ == '__main__':
    n = int(input())
    if n>=1 and n<=150:
        for i in range(n):
            print (i+1,end="")
