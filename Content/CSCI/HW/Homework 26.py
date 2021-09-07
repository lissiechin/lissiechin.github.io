## Lissie Chin
## Homework 26
## Due May 10, 2019

## 1 – Tower of Hanoi
###Tower of Hanoi puzzle:
###  Let disk 1 be the smallest, disk 2 be the second-smallest, etc.
###  Let the posts be labeled 1, 2, 3.
###  Disks start on post 1, and end on post 3.
###  HINT: If called with n, start, and end
###   Base case: if n == 1
###       Move disk n from start post to end post
###   Otherwise:
###       Step 0: calculate which is the temp post WHAT??@E>#R$#TRTJSK$LTAKSJDTHLTWASJTDKSYAHLGRQFAEB<F
###       Step 1: recursive call to move n-1 disks from start post to temp post
###       Step 2: move disk n from start post to end post
###       Step 3: recursive calle to move n-1 disks from temp post to end post
##
#recursive function to PRINT the steps required to move the n-smallest disks
#  from the "start" post to the "end" post
def towerOfHanoi(n, start, end):
      middle = 2
      if n == 1:
            ## source to destination
            print ("move disk 1 from post {} to post {}".format(start, end))
      else:
            print ("move disk {} from post {} to post {}".format (n-1, start,middle))
            print ("move disk {} from post {} to post {}".format (n-1, middle,end)) 

                
                                                                                        ##### IDK ############

#now start the program
num = int(input("How many disks? "))
towerOfHanoi(num, 1, 3)
# The above call will print the following sequence:
#  Move disk 1 from post 1 to post 3
#  Move disk 2 from post 1 to post 2
#  Move disk 1 from post 3 to post 2
#  Move disk 3 from post 1 to post 3
#  Move disk 1 from post 2 to post 1
#  Move disk 2 from post 2 to post 3
#  Move disk 1 from post 1 to post 3
print("DONE")



## 2 – Binary search algorithm
      # function requires alist to be sorted in ascending order
      # Returns TRUE if in alist  & FALSE otherwise
      # USE RECURSION!!

      ## If the list is empty, then return False.
      ## Otherwise, look at the middle item in the list; if that is
            ## the desired item, then return True.
      ## Otherwise, recursively search either the left half or the right
            ## half of the list, depending on whether the desired item is greater than or
            ## less than the middle item of the current list.


def binarySearch (alist, item):      
      if item in alist:
            return True
      else:
            return False
      if len(alist) == 0:
            return False
      else:
            center = len(alist)//2
            if alist[center] == item:
                  return True
            else:
                  for i in range (len(alist)):
                        if alist[i] > item:
                              alist[center:]
                        else:
                              alist[:center]



## 3 – Questions

## What is the smallest number of moves that will
## solve the Tower of Hanoi problem for 4 disks?
      #2**n -1
      # 2**4 -1 = 15 moves

## What is the smallest number of moves that will solve the
## Tower of Hanoi problem for n disks? (Your answer will be an expression that depends on n.)
      # 2**n -1 (n = number of disks)

      
## Suppose you have a sorted list of 7 items. If you do a binary search on this list,
## what is the maximum number of items in the list that will need to be examined before the s earch algorithm can return True or False?
      ## 4 

      
## What is the size of the largest list such that a binary search on the list will
## always return True or False by examining no more than 5 items in the list?
      # 10
      
