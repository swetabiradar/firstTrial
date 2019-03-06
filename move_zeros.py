#!/usr/bin/env python

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

class Solution:
      def __init__(self,nums):
          self.nums = nums
    
      def moveZeros(self):
          self.nums = sorted(self.nums)
          while self.nums[0] == 0:
                self.nums.pop(self.nums[0])
                self.nums.append(0)
          return(self.nums)


nums = raw_input('Enter list here:')
nums = (int(n) for n in nums)
a = Solution(nums)
print(a.moveZeros())

