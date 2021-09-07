## Lissie
## Homework 18
## Due April 17,2019

## 1 – Add to Point cass method is_origin
##    returns True if point has cordinates (0,0) and False otherwise

class Point:
      def __init__ (self, x, y):
            self.xcord = int(x) 
            self.ycord = int(y)

      def getX (self):
            return self.xcord
      
      def getY (self):
            return self.ycord
      
      def is_origin (self):
            if self.xcord == 0:
                  if self.ycord == 0:
                        return True
                  return False
            return False
                              ## 2 – add slope_from_origin
      def slope_from_origin (self):
            deltaX = self.xcord - 0
            deltaY = self.ycord - 0
            if deltaX == 0:
                  return None
            else:
                  slope = float  (deltaY/deltaX)
                  return slope

                              ## 3 – add reflect_x that returns a new Point which
                              ##    is the reflection across the x-axis
      def reflect_x (self):
            newPointX = self.xcord
            newPointY = -(self.ycord)
            newPoint = (newPointX, newPointY)
            return newPoint

                              ## 4 – add a method move that takes two parameters (dx / dy )
                              ##    method will modify properties so the point MOVES given distances
      def move (self, dx, dy):
            self.xcord = self.xcord + dx
            self.ycord = self.ycord + dy
            return str(self.xcord) + "," + str(self.ycord)
                              ## 5 – add a method that "adds" two points by adding corresponding c- and y-
                              ##    coordinates

      def adds (self, nX, nY):
            self.xcord = self.xcord + nX
            self.ycord = self.ycord + nY

            return str(self.xcord) + "," + str(self.ycord)



            
p = Point(6,3)
print(p.is_origin())       
print(p.slope_from_origin())
print(p.reflect_x())
print(p.move(3,4))
print(p.adds(-4,8))                 ## adding to the (9,7) from move method



w = Point(1,-1)
print(w.adds(4,3))

##np = Point (0,0)
##print(np.is_origin())       
##print(np.slope_from_origin())
##print(np.reflect_x())
##print(np.move(3,4))
##print(np.adds(-4,8))


##q = Point (1,6)
##print(q.is_origin())       
##print(q.slope_from_origin())
##print(q.reflect_x())
##print(q.move(3,4))
##print(q.adds(-4,8))




