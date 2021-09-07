#Lissie
#Homework 4 : 5.6 exercises 16, 17, 18
# Due 20 Feb 2019

#16
import random
for i in range(10):
    print(i)

#17
import random
for i in range(25,36):
    print(i)

#18
import math
a = int(input("what is the height?"))
b = int(input("what is the base length?"))
c = math.hypot(a,b)
print (c)




#length of the third side if 2 sides and 1 angle are known

import math
a = int(input("length of side a"))
b = int(input("length of side b"))
angleD = int(input("what is the angle, in degrees, between a and b?"))
angleR = math.radians(angleD)
c = math.sqrt(a**2 +b**2 -(1*a*b*math.cos(angleR)))
print (c)
        
