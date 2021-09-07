## Lissie
## Hw 9 –– 7, 8, 10, 11, 12
## Due: March 11, 2019


##7 – get rid of the red in the image
from cImage import*
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

def remove_red(myImage):
    for row in range(myImage.getHeight()):
        for col in range(myImage.getWidth()):
            p = myImage.getPixel(col,row)
            
            r = 0
            g = p.getGreen()
            b = p.getBlue()
            
            newPixel = image.Pixel(r, g, b)
            myImage.setPixel (col, row, newPixel)
            
img.draw(remove_red(img))
win.exitonclick()


## 8 – Grayscale

import image
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

def grayscale (myImage):
    for row in range(myImage.getHeight()):
        for col in range(myImage.getWidth()):
            p = img.getPixel(col,row)
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
            Scale = (red + green + blue)/3
            newR = Scale
            newG = Scale
            newB = Scale
            
            newP = image.Pixel(newR, newG, newB)
            myImage.setPixel (col, row, newP)
img.draw(grayscale(img))
win.exitonclick()


## 10 – Sepia Tone

import image
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

def grayscale (img):
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col,row)
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
            newR = (red*0.93 + green*0.769 +blue*0.189)
            newG = (red * 0.349 + green * 0.686 + blue * 0.168)
            newB = (red * 0.272 + green * 0.534 + blue * 0.131)
            
            newP = image.Pixel( newR, newG, newB)
            img.setPixel (col, row, newP)
#img.draw(grayscale(img))
#win.exitonclick()


## 11 – englarge image

#import image

def double (oldimage):
    nImg = image.EmptyImage(oldimage.getWidth()*2,oldimage.getHeight()*2)               ## dimensions will be flipped if Height goes before Width = problem for resizing
    for row in range(oldimage.getHeight()):                                         ## speeds up how its processed, putting row before col in for loop
        for col in range(oldimage.getWidth()):
            oldPix = oldimage.getPixel(col, row)
            nImg.setPixel(col*2,row*2, oldPix)
            nImg.setPixel(col*2 +1, row*2, oldPix)
            nImg.setPixel(col*2, row*2+1, oldPix)
            nImg.setPixel(col*2+1, row*2+1, oldPix)
    return nImg

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth()*2, img.getHeight()*2)

DrawBig =double(img)
DrawBig.draw(win)

#win.exitonclick()



##12 – Average pixels around it to make it less blocky (based off 11)


def dubnsmooth (oldimage):
    nImg = image.EmptyImage(oldimage.getWidth()*2,oldimage.getHeight()*2)               ## dimensions will be flipped if Height goes before Width = problem for resizing
    for row in range(oldimage.getHeight()):                                         ## speeds up how its processed, putting row before col in for loop
        for col in range(oldimage.getWidth()):
            oldPix = oldimage.getPixel(col,row)
            
            nImg.setPixel(col*2,row*2, oldPix)
            nImg.setPixel(col*2 +1, row*2, oldPix)
            nImg.setPixel(col*2, row*2+1, oldPix)
            nImg.setPixel(col*2+1, row*2+1, oldPix)
            
            oldPix0 = oldimage.getPixel(col*2,row*2)
            oldPix1 = oldimage.getPixel(col*2 +1, row*2)
            oldPix2 = oldimage.getPixel(col*2, row*2+1)
            oldPix3 = oldimage.getPixel(col*2+1, row*2+1)
            
            newRed = (oldPix0.getRed()+oldPix1.getRed() + oldPix2.getRed() + oldPix3.getRed())//4         ## average color & int divide
            newGreen = (oldPix0.getGreen() +oldPix1.getGreen() + oldPix2.getGreen() + oldPix3.getGreen())//4
            newBlue = (oldPix0.getBlue() +oldPix1.getBlue() + oldPix2.getBlue() + oldPix3.getBlue())// 4
            newPix = image.Pixel(newRed, newGreen, newBlue)   
            nImg.setPixel(col*2,row*2, newPix)
            nImg.setPixel(col*2+1,row*2, newPix)
            nImg.setPixel(col*2,row*2+1, newPix)
            nImg.setPixel(col*2+1,row*2+1, newPix)
            
    return nImg

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth()*2, img.getHeight()*2)

DrawBig = dubnsmooth(img)
DrawBig.draw(win)

win.exitonclick()




#def main():
#    print ("starting")
##    win = ImageWin("My Window",1070,760)
##    oImage = FileImage('luther.gif')
##    print(oImage.getWidth(), oImage.getHeight())
##    oImage.draw(win)
##    myImage1 = oImage.copy()
##    myImage2 = oImage.copy()
##    myImage3 = oImage.copy()
##    myImage4 = oImage.copy()
##
##    remove_red(myImage1)        
##    myImage1.setPosition(myImage1.getWidth()+10,0)
##    myImage1.draw(win)
##
##    grayscale(myImage2)
##    myImage2.setPosition(0, myImage2.getHeight()+10)
##    myImage2.draw(win)
##    
##
##    double(myImage3)
##    myImage3.setPosition(myImage3.getWidth()+10, myImage3.getHeight()+10)
##    myImage3.draw(win)
##
##    dubnsmooth(myImage4)
##    myImage4.setPosition(myImage4.getHeight()+20)
##    myImage4.draw(win)


