#!/usr/bin/env python

""" creatng linked List """

class Node:
      def __init__(self,dataval=None):
          #assert type(dataval) is str, 'Node.__init__: data('+str(dataval)+') must be a string'
          self.dataval = dataval
          self.nextval = None
      """
      def getDataval(self):
          return self.dataval
      def getNextval(self):
          return self.nextval
      """
class SlinkedList:
      def __init__(self):
          self.headval = None 
      """
      def getHeadval(self):
          return self.headval
      """
      def listprint(self):
          printval = self.headval
          while (printval):
                print(printval.dataval)
                printval = printval.nextval 

Llink = SlinkedList()
Llink.headval = Node("Mon")
e1 = Node("Tue")
e2 = Node("Wed")

Llink.headval.nextval = e1
e1.nextval = e2

print('Llink = {}, Llink.headval = {},e1 = {}, e2 = {}'.format(Llink.__dict__,Llink.headval,e1,e2))
Llink.listprint()

