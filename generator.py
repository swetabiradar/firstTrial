#!/usr/bin/env python3

def main():
 for i in inclusive_range(5,25,5):
  print(i,end=' ')
 print()
def inclusive_range(*args):
 numargs = len(args)
 start = 0
 step = 1
 
 if numargs < 1:
  raise TypeError('at least 1 argument expected, got {numargs}')
  
 elif numargs == 1:
  stop = args[0]
 
 elif numargs == 2:
  (start,stop) = args
 
 elif numargs == 3:
  (start,stop,step) = args

 else:
  raise TypeError('too many arguments, got{numargs}')

 #genertaor
 
 i = start
 while i <= stop:
  yield i
  i += step
  
if __name__ == '__main__':
 main()
  
 
  
