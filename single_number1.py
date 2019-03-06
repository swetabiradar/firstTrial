#!/usr/bin/env python

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

"""

class Solution:
      def __init__(self,nums):
          self.nums = nums 

      def singleNumber(self):
          check = []
          
          for num in self.nums:
              if num not in check:
                 check.append(num)
              else:
                 check.remove(num)
      
          return (check.pop())


nums = (raw_input('Enter list:'))
#nums.split()
nums = [int(num) for num in nums]
a = Solution(nums)
print(a.singleNumber()) 
