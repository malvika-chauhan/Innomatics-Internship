'''

Print the palindromic triangle of size  as explained above.



'''
for i in range(1,int(input())+1):
    print (((10**i - 1)//9)**2)
