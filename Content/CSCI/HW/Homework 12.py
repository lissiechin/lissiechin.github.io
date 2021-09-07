## Lissie
## Homework 12: 2, 4, 6, 8, 10, 12
## Due April 3, 2019


## 2 – list with six items: 76, 92.3, “hello”, True, 4, 76.

      ## with append, concatenation, one at a time
myList = []
myList.append(78)
myList.append(92.3)
myList.append("hello")
myList.append(True)
myList.append(4)
myList.append(76)
print (myList)



## 4 – list containing 100 random int numbers between 0-1000

import random

def average():
    intList = []
    for i in range(101):
        x = int(random.randrange(0,1000))
        intList.append(x)
    return intList
print(average())



## 6 – sum_of_squares(xs)

def sum_of_squares(xs):
    sum = 0
    for i in xs:
        square = i**2
        sum += square
    return sum
sum_of_squares([2,3,4])



## 8 – Sum up all even numbers in a list

##def sumEven(alist):
##    blist = [summ += num for num in alist if num %2 == 0]
##    return summ
##sumEven([2,3,4,5,6,7,8,9,10])




## 10 – Count how many words in a list have a length of five

def countWords(lst):
    cnt = []
    for i in lst:
        if len(i) == 5:
              cnt.append(i)
    count = len(cnt)
    return count
lst =  ["hello", "thanks", "hello", "7", "4", "6","thank", "faded", "noise", "no"]
print(countWords(lst))



## 12 – Count how many words occur in a list up tp and including the first occurence
      ## of the word "sam"
print ("starting 12")
import string
def findSam (senten):
    new = senten.split()
    idx = 0
    for i in new:
        if new[idx] == "sam":
            print ("this is the number to enter:",idx)
        idx += 1
def count(senten):
    findSam(senten)
    lst = senten.split()
    idx = int(input("number above"))
    cnt = lst[:idx+1]                           # plus "sam" (+1) since it stops one before  
    print (cnt)
    return len(cnt)


senten = "hello oh shell samee no thanks testing testing sam bubble no" 
print (count(senten))










##def count(lst):
##    count = 0
##    findsam = False
##    for i in lst:
##        if i != "sam" and findsam != True:
##            count += 1
##        else:
##            findsam = True
##                 
##    return count+1                ## add one to include the first occurence of
##                                  ## sam
##
##
##lst = [ "hello", "oh","shell", "samee", "sam","bubble", "no" ]
##print (count(lst))

