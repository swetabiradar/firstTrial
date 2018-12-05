#!/usr/bin/env python3

def our_decorator(func):
 print ('inside func '+func.__name__)
 def function_wrapper(x):
  print('Before calling func '+ func.__name__)
  func(x)
  print('After calling func'+func.__name__)
 return function_wrapper

def foo(x):
 print ('calling funct {} with string {}'.format(__name__,str(x)))

print ('calling func foo')

foo('hi')

print ('calling func our decorator')

foo = our_decorator(foo)
foo(42)
print (foo)
