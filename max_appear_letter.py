#!/usr/bin/env python3

"""
Write a function to return a letter, that occurs max no. of times in a given string, if two letters have same count then return a letter that occurs first in the string 
Ex: s = 'bbaaacc'  string s has 'a','b' and 'c','a' appear 3 times, then return 'a' as it appears maximum times
Ex: s = 'bbbaaaccc'  string s has 'a','b' and 'c', appear 3 times, then return 'b' as it appears firstEx: s = 'abbbbaaaccc' string s has 'a','b' and 'c', 'a' and 'b' appear 4 times, then return 'a' as ## it appears first
"""

def max_letter(s):
  ##returns a letter##
  if s == '':
    return 0

  temp_dict = {}
  """
  for c in range(len(s)):
    if s[c] not in temp_dict:
       temp_dict[s[c]] = 1
    else:
       temp_dict[s[c]] += 1
  """
  for c in range(len(s)):           # c is the index of that letter in string  
    if s[c] not in temp_dict:
       temp_dict[s[c]] = [1,c]      # storing count and index of that letter as list,value for key  
    else:                           # index is only the first occurence of that letter in the string
       temp_dict[s[c]][0] += 1      # updating count,the  first element of value list 

  print(temp_dict)
  
  temp_v = [0,0]                # Temp Value  
  temp_k = ''                   # temp Key
  
  for k,v in temp_dict.items():
      
      if (v[0] > temp_v[0]):    # comparing count of letter in a string
          max_k = k             # assigning key to the max_k, if current key has max count 
          temp_v = v            # updating temp_v and temp_k with current k,v
          temp_k = k

      elif (v[0] == temp_v[0]):   # if two keys have same count, return a key which appears first the string
          if (temp_v[1] < v[1]):
             max_k = temp_k
          else:
             max_k = k
      else:
          max_k = temp_k
    
    
  return max_k

def main():
 s = "abbbbgggggggggaaaa"
# s = ''
 a = max_letter(s) 
 print (a)

main()
