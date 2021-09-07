#Lissie
# Homework 5: 1, 2, 8, 10
# 22 Feb 2019


# Write a fruitful function sumTo(n)

def sumTo(n):
    for i in range (1, 11):
        int_sum = int((n*(n+1))/2)
    return int_sum
a = sumTo(10)
print(a)


#1
import turtle
wn = turtle.Screen()
boba = turtle.Turtle()
def drawLayerSquare (x,sz):
    for i in range (4):
        x.forward(sz)
        x.right(90)
for i in range (5):
    drawLayerSquare(boba,20)
    boba.penup()
    boba.forward(40)
    boba.pendown()
boba.reset()
    
#2


def drawLayerSquare (x,size):
    for i in range (4):
        x.forward(size)
        x.right(90)
size = 20
for i in range (4):
    drawLayerSquare(boba,size)
    size = size + 20
    boba.penup()
    boba.goto(boba.pos() + (-10,10))
    boba.pendown()
boba.reset()

#8
def areaOfCircle(r):
    import math
    area = math.pi * (r **2)
    return area
print(areaOfCircle(12)) 

#10

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

for i in range (5):
    drawFivePointStar(boba)
    boba.penup()
    boba.forward(350)
    boba.right(144)
    boba.pendown()
wn.exitonclick()

