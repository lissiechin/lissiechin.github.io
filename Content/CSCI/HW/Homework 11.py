## Lissie
## Homework 11
## Due 15 March 2019

## 1 – Write a function that counts how many times a substring occurs in a string. 

import string
def countOccurrences (bigstr,substr):
      x = 0                         # current index location
      numlet = 0
      sslen = len(substr)           #
      while x < len(bigstr):
            if bigstr[x:x+sslen] == substr:
                  numlet += 1
                  x += sslen
            
            else:
                  x += 1             #move over 1 index                    
      return numlet
bigstr = input("enter a word")
substr = input(" enter part of the word or letter which you want to know how many times it occurs in the word")
print(countOccurrences(bigstr, substr))

## 2 – Write a function that removes all occurrences of a string from another string.

def removeAll(mystr,sub):
      idx = 0
      nStart = 0
      while idx < len(mystr) and idx != -1:
            idx = mystr.find(sub, idx)
            if idx >= 0:
                  mystr = mystr[:idx] + mystr[idx+1:]
      idx = nStart
      print(mystr)
      return removeAll

mystr = "mississippi"
sub = "s"
removeAll(mystr,sub)


## 3 – Write a function that converts a word to pig Latin.
      ## If the word begins with a consonant, then all letters before the initial vowel
      ## are moved to the end of the word, and then “ay” is added to the end. For example,
      ## “pig” becomes “igpay”, and “glove” becomes “oveglay”.

      ##If the word begins with a vowel, then add “yay” to the end. For example, “eat” becomes “eatyay”.
def findVowel (astr):
      idx = 0
      vowel = "aeiou"
      found = False
      while idx <len(astr) and not found:
            if astr[idx] in vowel:
                  found = True
            else:
                  idx += 1
                        
      if found:
            print (idx)

def OPIgpay (word):
      V = "aeiou"
      igpayTransl = ""
      if word[0] not in V:
            findVowel(word)
            idx = int(input("enter the number that appears above"))
            igpayTransl = word[-(len(word)-idx):] + word[:idx] + "ay"
            print("in pig latin it's:",igpayTransl)
      else: 
            igpayTransl = word + "yay"
            print("in pig latin it's:", igpayTransl)

word = input("enter a word")
OPIgpay(word)


## 4 – Write a function to that recognizes an email address. That is, write a function called
## isEmailAddress that takes a string argument and returns True if the string is a properly-formatted
## email address, and False otherwise.
      ##The format of an email address is local_part@domain.

def occurrence (email,char):
      x = 0                     
      count = 0
      sslen = len(char)       
      while x < len(email):
            if email[x:x+sslen] == char:
                  count += 1
                  x += sslen
            else:
                  x += 1                       
      return count

def isEmailAddress (email):
      SymbCheck = occurrence(email,"@")
      domainCheck = occurrence(email,".net")
      if (SymbCheck == 1) and (domainCheck == 1):
            print ("True")
      elif (SymbCheck !=1) and (domainCheck != 1):
            print ("False")
      else:
            print ("True")


##def isEmailAddress (email):
##      if occurrence(email,"@") > 1 and occurrence(email,".net") > 1:
##            return False
##      return True

isEmailAddress("cool-address!@mydomain.net")
isEmailAddress("me@domain@net")
isEmailAddress("notAnEmailAddress")







