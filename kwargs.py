#!/usr/bin/env python3

def main():
 x = dict(hi='hello', go = 'going', bye= 'cya')
 kitten (**x)

def kitten(**kwargs):
 if len(kwargs):
  for k in kwargs:
   print('kitten {} does {}'.format(k,kwargs[k]))
 else:
   print ('meow')

if __name__  == '__main__':
 main()
