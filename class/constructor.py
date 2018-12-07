#!/usr/bin/env python3

class animal():
 def __init__(self,**kwargs):
  self._type = kwargs['type'] if 'type' in kwargs else 'No type'
  #self._type = kwargs['type'] 
  self._name = kwargs['name'] if 'name' in kwargs  else 'No name'
  #self._name = kwargs['name'] 
  self._sound = kwargs['sound'] if 'sound' in kwargs else 'No sound'
  #self._sound = kwargs['sound'] 

 def type(self):
  return self._type
 
 def name(self):
  return self._name
 
 def sound(self):
  return self._sound
 
 def __str__(self):
  return f'the {self.type()} is animal name {self.name()} and makes sound {self.sound()}'

def print_animal(o):
 if not isinstance(o,animal):
  raise TypeError('print_animal(): requires an animal')
 else:
  print(f'the {o.type()} is animal name {o.name()} and makes sound {o.sound()}')

def main():

 a1 = animal(type = 'kitten',sound = 'meow', name= 'tweety')
 a2 = animal(type = 'monkey',name = 'titu', sound= 'grrr')
# print_animal(a1)
 print(a1)
 print(a2)
 print_animal(a2)
 print_animal(animal())
 print_animal()
 #print_animal( animal(type = 'kitten',sound = 'meow', name= 'tweety'))

if __name__ == '__main__':
 main()
