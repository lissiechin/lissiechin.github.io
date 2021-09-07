## Lissie Chin
## Homework 15
## Due: 4.10.19

## 1.  Complete the pirateTranslator function from class.  The description
## is provided in the attached file.

import string


def removeNonAlpha (astr):
      nS = ""
      for c in astr:
            if c.isalpha():
                  nS += c
      return nS

def pirateTranslator(pirateDictionary, inputString):
      newString = ""
      inputString = inputString.split()
      
      new =[removeNonAlpha(word) for word in inputString]
 
      for item in new:
            if item in pirateDictionary:
                  newString += str(pirateDictionary[item]) + " "
            else:
                  newString += item + " "
      return newString

pirateWords = {"Hello":"Ahoy", "friend":"matey", "friends":"mateys", \
               "hello":"ahoy", "are":"be", "you":"ye", "my":"me"}
print(pirateTranslator(pirateWords, "Hello, how are you?")) #Ahoy how be ye



## 2.  Write a function merge(d1, d2) that merges two dictionaries and returns the result. Any key that
## appears in d1 or d2 should appear in the returned dictionary. If a key appears in ONLY ONE of d1 or d2,
## then its value in the returned dictionary should be the same as its value in d1 or d2. However, if a key
## appears in BOTH d1 and d2, then its value in the returned dictionary should be the sum of its values in d1 and d2.

## For example:

d1 = {'a':5, 'b':2}

d2 = {'a':3, 'c':4}

## merge(d1,d2) # should return {'a':8, 'b':2, 'c':4}.


def mergeList (d1, d2):
      copy = d1.copy()
      for i in d2:
            if i in copy and i in d2:
                  copy[i] += d2[i]
            else:
                  copy[i] = d2[i]
      return copy
      

d1 = {'a':5, 'b':2}
d2 = {'a':3, 'c':4}
print (mergeList(d1,d2))
