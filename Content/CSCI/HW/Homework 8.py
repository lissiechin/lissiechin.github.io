##Lissie
## Homework 8 –  2, 4, 5, 6
## Due: March 6, 2019



####    2 Triangle Numbers
def print_triangular_numbers(n):
    for i in range (1,n+1):
        t = (i*(i+1))/2
        print (i, '\t', t)
n = int(input("enter a number to find its triangular number"))
print_triangular_numbers(n)



#####        4: Turtle moving randomly
import random
import turtle


boba = turtle.Turtle()
wn = turtle.Screen()

boba.shape('turtle')
boba.color('blue')
boba.speed(30)



def isInScreen(w,t):
      xmin = -wn.window_width()/2
      xmax = wn.window_width()/2
      ymin = -wn.window_height()/2
      ymax = wn.window_height()/2

      x = t.xcor()
      y = t.ycor()

      if x < xmin or x > xmax:
            return False
      if y < ymin or y > ymax:
            return False
      return True


while isInScreen (wn,boba) == True:
      boba.fd(50)
      coin = random.randrange(0,2)
      if coin == 0:
            l = random.randrange(0,360)
            boba.left(l)
      else:
            r = random.randrange(0,360)
            boba.right(r)
boba.reset()


#####      5–  two turtles keep walking until one leaves the screen

def random_Walking(anyturtle,distance):
      anyturtle.fd(distance)
      coin = random.randrange(0,2)
      if coin == 0:
            l = random.randrange(0,360)
            anyturtle.left(l)
      else:
            r = random.randrange(0,360)
            anyturtle.right(r)

def turtle_Colliding(turtle1, turtle2):
      T1_position = turtle1.pos()
      T2_position = turtle2.pos()
      if T1_position - T2_position <= 2:
            return True
      return False
    

def isInScreen(w,t):
      xmin = -wn.window_width()//2
      xmax = wn.window_width()//2
      ymin = -wn.window_height()//2
      ymax = wn.window_height()//2

      x = t.xcor()
      y = t.ycor()

      if x < xmin or x > xmax:
            return False
      if y < ymin or y > ymax:
            return False
      return True


tootsie = turtle.Turtle()
tootsie.shape('turtle')
tootsie.color('green')


xmin = -wn.window_width()/2
xmax = wn.window_width()/2
ymin = -wn.window_height()/2
ymax = wn.window_height()/2


tootsie.penup()
tootsie.goto(random.randrange(int(xmin),int(xmax)), random.randrange(int(ymin),int(ymax)))
tootsie.pendown()


while isInScreen(wn,boba) and isInScreen(wn,tootsie):
            random_Walking(boba,100)
            random_Walking(tootsie, 200)

boba.reset()
tootsie.reset()


###   6 bounce turtle back inside screen

tootsie.color('blue')

def random_Walking(anyturtle,distance):               # moving a turtle x amount of distance
      anyturtle.fd(distance)                          # and turning a random degree left or right
      coin = random.randrange(0,2)
      if coin == 0:
            l = random.randrange(0,360)
            anyturtle.left(l)
      else:
            r = random.randrange(0,360)
            anyturtle.right(r)

def turtle_Colliding(turtle1, turtle2):               # distance of two turtle's position 
      if turtle1.distance(turtle2) < 1:
            return True
      return False
    
def isInScreen(w,t):
      xmin = -wn.window_width()/2
      xmax = wn.window_width()/2
      ymin = -wn.window_height()/2
      ymax = wn.window_height()/2
      x = t.xcor()
      y = t.ycor()

      if x < xmin or x > xmax:
            return False
      if y < ymin or y > ymax:
            return False
      return True

def Turtle_wall(w,t):                     #Find out if turtle will be going off the screen
      isInScreen(w,t) 
      xmin = (-wn.window_width()/2) +10
      xmax = (wn.window_width()/2)-10
      ymin = (-wn.window_height()/2)+10
      ymax = (wn.window_height()/2)-10

      x = t.xcor()
      y = t.ycor()
      while isInScreen(w,t) == True:
            if (x - xmin < 1) or (x - xmax < 1) or (y - ymin < 1) or (y-ymax < 1):
                  return True
            else:
                  return False
            return Turtle_wall


xmin = -wn.window_width()/2
xmax = wn.window_width()/2
ymin = -wn.window_height()/2
ymax = wn.window_height()/2


tootsie.penup()
tootsie.goto(random.randrange(int(xmin),int(xmax)), random.randrange(int(ymin),int(ymax)))
tootsie.pendown()
                                                            # call other functions & check               
               
while True:
      random_Walking (boba, 80)
      random_Walking (tootsie, 80)
      
      if turtle_Colliding (boba,tootsie) == True:
            boba.right (180)
            boba.forward(100)
            random_Walking(boba,80)
            tootsie.left (180)
            tootsie.forward(100)
            random_Walking(tootsie, 80)

      if Turtle_wall(wn,boba) == False:
            boba.right (180)
            boba.forward(100)
            
      if Turtle_wall(wn,tootsie) == False:
            tootsie.right(180)
            tootsie.forward(100)

wn.exitonclick()
      
