'''
The provided code stub reads two integers a,b from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    if (a>=1 and a<=pow(10,10)) and (b>=1 and b<=pow(10,10)):
        print(a+b)
        print(a-b)
        print(a*b)
