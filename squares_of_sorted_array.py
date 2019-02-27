#!/usr/bin/env python


class Solution():
      def __init__(self,A):
          self._A = A 
      def sortedSquares(self):
          return sorted(x*x for x in self._A)


def main():
    list1 = [-1,-2,2,3]
    a = Solution(list1)
    print('reversed list is {}'.format(a.sortedSquares()))

if __name__ == '__main__':
    main()

