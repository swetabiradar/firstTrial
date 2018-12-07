#!/usr/bin/env python3
class Solution:
    
    def __init__(self,nums,target):
        self._nums = nums
        self._target = target

    def twoSum(self):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(self._nums)
        if l >1:
                for i,val in enumerate(self._nums):
                         for j,val1 in enumerate(self._nums[i+1:l],start=i+1):
                            if val == self._target - val1:
                               return [i,j]
                         
        else:
                print('Atleast 2 arguments are needed')
           

    
def main():
 l = [2,2,2,2]
 t = 4
 sum1 = Solution(l,t)
 a = sum1.twoSum()
 print('list ={}, target = {}'.format(l,t))
 print(a) 
if __name__ == '__main__':
 main()
