'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for i in nums:
            out+=[curr+[i] for curr in out]
        return out