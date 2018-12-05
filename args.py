#!/usr/bin/env python3

def main():
 x = ('hi','hello','world')
 kitten(*x)

def kitten(*args):
 if len(args):
  for s in args:
   print (s)
 else:
   print ('meow')

if __name__ == '__main__':
 main()
 
