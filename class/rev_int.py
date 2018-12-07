#!/usr/bin/env python3

class Solution:

    def __init__(self,x):
        self._x = x
    def reverse(self):
        """
        :type x: int
        :rtype: int
        """
        new_num = 0
        mod_num = 0
        x1 = abs(self._x)
        while (x1 != 0):
                mod_num = x1 % 10
                x1 = x1//10
                new_num = (new_num*10) + mod_num
                
        
        if (new_num in range((2**31-1))):

            if self._x < 0:
                return -new_num
            else:
                return new_num
        else:
            print('reversed number is out of range [-2^31 : 2^31-1]')
            return 0

def main():
 num = 21474
 print('number is {}'.format(num))
 a = Solution(num)
 print('reversed number is {}'.format(a.reverse()))

if __name__ == '__main__':
 main()
