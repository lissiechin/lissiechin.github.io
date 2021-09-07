### Lissie Chin
### Homework 2 (#7,8, 10, 12)
### Due February 15, 2019


#problem 7 

P = 10000
n = 12
r = 8/100
t = int(input ("number of years"))  

Final_Amount= P*( 1 + (r/n))**(n*t)

print ("The final amount after", t, "years is $", Final_Amount)



#problem 8

R= int(input("radius of the circle"))
Pi= 3.14159265359 
Area= Pi*(R**2)
print ("The area of the circle is", Area)


#problem 10

M = int(input("miles driven?"))
G = int(input("gallons used"))

Total = M/G
print ("Your car's MPG is", Total)


#problem 12

Temp = int(input("What is the degrees Fahrenheit?"))
C = (Temp - 32)* (5/9)
print ("If it is",Temp, "degrees Fahrenheit, then it is", C, "degrees Celsius.")
