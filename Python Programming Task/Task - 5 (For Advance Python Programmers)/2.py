'''

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 
 
 '''
 
 class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = 0
        res = int(x)^int(y)
        for i in range(32):
            if((res>>i)&1==1):
                a+=1
        return(a)