'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if(nums.count(nums[i])==1):
                break
        return(nums[i])
                