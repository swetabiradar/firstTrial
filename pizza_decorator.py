#!/usr/bin/env python3

def logger_events(func):
 def wrapper(*args):
  print ('ordering '+func.__name__)
  func(*args)
 return wrapper

@logger_events
def pizza(*toppings):
 args = ' '
 for x in toppings:
  args = args + x +','
 
 print('adding'+ str(args)+ 'to'+ pizza.__name__)

pizza('cheese') 

