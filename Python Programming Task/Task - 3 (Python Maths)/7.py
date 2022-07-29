'''

You are given a positive integer . Print a numerical triangle of height  like the one below:

1
22
333
4444
.....
'''

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i-1)//9*i)
