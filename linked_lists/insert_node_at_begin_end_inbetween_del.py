#!/usr/bin/env python

class Node:
      def __init__(self,dataval):
          self.dataval = dataval
          self.nextval = None

class Slinked:
      def __init__ (self):
          self.headval = None

      def printlist (self):
          printval = self.headval
          while(printval):
               print(printval.dataval)
               printval = printval.nextval
   
      def atBegin(self,newdata):
          newNode = Node(newdata)
          newNode.nextval = self.headval
          self.headval = newNode

      def atEnd(self,newdata1):
          newNode = Node(newdata1)
          if self.headval is None:
             self.headval = newNode
             return
          curr_node = self.headval
          while(curr_node.nextval):
               curr_node = curr_node.nextval
          curr_node.nextval = newNode

      def inBetween(self,node1,node2,newdata):
         newNode = Node(newdata)
         if node1 is None:
            print('Provide first node')
            return
         if node2 is None:
            #print('provide second node')
            node2 = self.headval.nextval

         newNode.nextval = node2
         node1.nextval = newNode

      def delNode(self,node):
          if self.headval.nextval is None:
             return None
          elif node.dataval == self.headval:
             self.headval = self.headval.nextval
          else :
             node.dataval  = node.nextval
            
                   
# creating linked list 
list = Slinked()
list.headval = Node("Mon")
e1 = Node("Tue")
e2 = Node("Wed")
list.headval.nextval = e1
e1.nextval = e2

#adding new node at the beginning of linked list
list.atBegin("Sun")
list.atBegin("Sat") 

#adding new node at the end of linked list
list.atEnd("Thu")

#adding new node in between two nodes 
node1 = list.headval.nextval
node2 = node1.nextval
list.inBetween(node1,node2,"Fri")

#deleting a node from linked list
node = list.headval.nextval
list.delNode(node)
list.delNode(node.nextval)
print('next node of sun = {}'.format(list.headval.nextval.nextval.dataval))

#printing linked list
list.printlist()
