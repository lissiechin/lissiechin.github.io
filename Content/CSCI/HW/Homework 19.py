## Lissie
## Homework 19: Section 17.6 –– 7,8, 10, 12
## Due April 19, 2019


## Part one ––––––––––––

## 7

class Po:
      def __init__ (self, initX, initY):
            self.x = initX
            self.y = initY

      def getX (self):
            return self.x

      def getY (self):
            return self.y
            

class Rec:
      def __init__(self, initlocation, initwidth, initheight):
            self.IL = initlocation
            self.IW = initwidth
            self.IH = initheight
                                          ## 8 – add accessor methods to the Rectangle class
      def getWidth (self):
            return self.IW
      
      def getHeight (self):
            return self.IH

      def __str__ (self):
            return "The rectangle's width is " + str(self.getWidth()) + " and it's height is " + str(self.getHeight())
      
                                          ## 10 – write a perimeter method
      def perimeter (self):
            return (2*self.IW) + (2*self.IH)


                                          ## 12 – Test if point falls within the rectangle method
      def inRec (self, x, y):
            X = str(self.getWidth())
            Y = str(self.getHeight())
            if 0 <= x < int(X) and 0 <= y < int(Y):
                  return True
            return False
            

r = Rec(Po(4,5),6,5)
print (r)
print (r.perimeter())
print (r.inRec(4,4))



p = Rec(Po(0, 0), 10, 5)
print(p.inRec(0, 0), True)
print(p.inRec(3, 3), True)
print(p.inRec(3, 7), False)
print(p.inRec(3, 5), False)
print(p.inRec(3, 4.99999), True)
print(p.inRec(-3, -3), False)

## Part 2 –––––––––––––––

class Robot:
      def __init__ (self, name, buildyear, batterylvl = 0):
            self.n = name
            self.by = buildyear
            self.bl = batterylvl

      def charge (self):
            return self.bl + 1

      def introduce (self):
            return "Hello, my name is " + self.n

      def __str__(self):
            return "robot name: " + self.n + ", the year " + self.by + "and battery life level " + self.bl

mike = Robot('Mike', 2016)
print (mike.introduce())
print(str(mike.bl()))
mike.charge()
print(mike.bl())
print(mike)
