## Lissie
## Homework 25
## Due: May 8th



## 1 – Recursive function reList(list1) that reverses the list
def reList(list1):
      if len(list1) == 0:
           return list1
      else:
            return reList(list1[1:]) + [list1[0]]
list1 = [True, 2, 'a']
print(reList(list1))

#### 2 – Palindrome: isPalindrome(inputString) determines if it is or not
def isPalindrome(inputString):
      if len(inputString) <= 1:
            return True
      if inputString[0] == inputString[-1]:
            return True
      else:
            return False
      
inputString = input("enter a word")
print(isPalindrome(inputString))


## 3 –Fibonacci sequence: recursive functino fibonacci(n) that computes the nth term of
##    of the fibonacci sequence

def fibonacci(n):
      if n < 1:
            return 0
      elif n == 1 or n == 2:
            return 1
      else:
            return fibonacci(n-1) + fibonacci(n-2)

n = 4
y = 15
print(fibonacci(4))
print(fibonacci(15))
