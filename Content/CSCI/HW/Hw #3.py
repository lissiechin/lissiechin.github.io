#Lissie
##Homework #3 (4, 6, 7, 10)
##Due: Feb 18 


#4
for i in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(i)
    print(i,i**2)

#6
import turtle
wn = turtle.Screen()
ray = turtle.Turtle()
ray.shape("turtle")
n = int(input("what is the number of sides?"))
length = int(input("what is the side length?"))
color = input("what color?")
fill_color = input("fill color?")
exteriorA = 360/n
ray.color(color)
ray.fillcolor(fill_color)
ray.begin_fill()
for i in range(n):
    print(i)
    ray.fd(length)
    ray.left(exteriorA)
ray.end_fill()

#7
import turtle
wn = turtle.Screen()
jackson = turtle.Turtle()
for i in (160, -43, 270, -97, -43, 200, -940, 17, -86):
    jackson.right(i)
    jackson.fd(50)
print("the pirate is currently heading southwest")

#10
import turtle
wn = turtle.Screen()
wn.bgcolor ("light green")
yay = turtle.Turtle()
yay.shape("turtle")
yay.color("blue")
for i in range(12):    
    print(i)
    yay.pu()
    yay.fd(70)
    yay.pd()
    yay.fd(20)
    yay.pu()
    yay.fd(30)
    yay.shape("turtle")
    yay.stamp()
    yay.pu()
    yay.fd(-120)
    yay.right(30)
wn.exitonclick()
