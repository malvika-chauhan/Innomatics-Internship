'''
Shuffle the Array
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 
'''
Sol 1:

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num = []
        l = m = n 
        for i in range(1,len(nums)+1):
            if i%2!=0:
                num.append(nums[l-n])
                l=l+1
            else:
                num.append(nums[m])
                m+=1
        return num
		
--------------------------------------------------

Sol 2:

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        for i in range(n):
            a.append(nums[i])
            a.append(nums[n+i])
        return a