#!/usr/bin/env python

"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
"""

class Solution:
    def __init__(self,words=[]):
        self.words = words

    def uniqueMorseRepresentations(self):
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_dict = {}
        
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']       
        
        i = 0
        
        while i < 26:
            #for alphabet in alphabets:
                morse_dict[alphabets[i]] = morse_list[i]
                i += 1
        
        
        
        morse_code = []
        
        
        # creating a list of morse code representation of each word in list of words 
        
        for word in self.words:
                morse_code_temp = ''
                for letter in word:
                    morse_code_temp += morse_dict[letter]
                morse_code.append(morse_code_temp)
        
        print(morse_code)
        #morse_code = list(dict.fromkeys(morse_code))  # removes duplicates from the list   
        # OR
        #morse_code = set(morse_code)
         
        morse_code = set(morse_code)
        return (len(morse_code))
    
words = ["gin", "zen", "gig", "msg"]
a = Solution(words)
print(a.uniqueMorseRepresentations())

