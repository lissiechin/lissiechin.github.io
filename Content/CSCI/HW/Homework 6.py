# Lissie
# Homework 6 – 1, 2, 6, and 8

#1
x = 3 == 3
print (x)
x = 3 != 3
print(x)
x = 3 >= 4
print (x)
x = not (3 < 4)
print(x)


# True  3 is equal to 3
# False  3 is not not equal to 3
#False  3 is not greater than or equal to 4
#False  The opposite of 3 < 4


#2
a = int(input("enter a number"))
b = int(input ("enter another number"))
day = int(input ("Day #?"))
# given statements
if(a > b):
    print("true")
else:
    print("false")

    
if(a >= b):
     print("true")
else:
    print("false")

    
if(a >= 18) and (day ==3):
     print("true")
else:
    print("false")
    

if(a >= 18) or (day!=3):
     print("true")
else:
    print("false")

#logical opposites

if(a < b):
     print("true")
else:
    print("false")
    
    
if(a <= b):
     print("true")
else:
    print("false")
    
    
if(a <= 18) or (day!= 3):
     print("true")
else:
    print("false")
    
    
if(a<= 18) and (day == 3):
     print("true")
else:
    print("false")

#6
import math
def findHypot(a,b):
    Hypo = float(math.sqrt((a**2) + (b**2)))
    return (Hypo)
c = findHypot(12,13)
print(c)

Side1 = 12
Side2 = 13
Hypoten = (Side1**2 + Side2**2)**0.5
print(Hypoten)




#8
def is_odd(n):
   if (n % 2) == 1:
        print ("odd")
   else: 
       print("even")
is_odd(5)
