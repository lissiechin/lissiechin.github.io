## Lissie
## Homework 24
## Due May 3, 2019

## 1 – HTML file that displays a color chart

import webbrowser, os.path

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()


#the following string stores the contents of a very basic HTML page

contents = '''<!DOCTYPE html>
<html>
<head>
  <title>Hello</title>
</head>
<body>
  <h1 style = "font-family: Impact; font-size: 60px; text-align: center;" > Colors </h1>
  '''

for red in range (0,226,15):
      r = red
      for green in range (0,226, 15):
            g= green
            for blue in range (0,226, 15):
                  b = blue
                  color = "#{:02x}{:02x}{:02x}".format(r,g,b)
                  contents += "<p style = 'color: white; font-family: Impact; border-style: solid; background-color:" + color + "; border-width: 18px; text-align: center;'>" + "Red" + str(r) + ", Green" + str(g) + ", Blue" + str(b) + '''</p>
                  <style>
                        p {background-color:''' + color +''';}
                  </style>
</body>
</html>
'''
#the filename for the HTML file to be created
filename = "helloWorld.html"

#write the HTML contents to a file
strToFile(contents, filename)

#open the HTML file in the default browser
webbrowser.open("file:///" + os.path.abspath(filename))



## 2 – enter a number. Your program should then write a HTML file
## that displays the first 8 powers (starting with the 0th power) of the number.

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()


#the following string stores the contents of a very basic HTML page

contents = '''<!DOCTYPE html>
<html>
<head>
  <title>Hello</title>
</head>
<body>
  <h1 style = "font-family: Impact; font-size: 60px" > Powers </h1>
  '''
number = int(input("enter a number you want to find the powers of"))
for power in range (9):
      product = number **power
      contents += "<p>" + str(number) + "<sup>" + str(power) + "</sup> = " + str(product) + '''</p>
      
</body>
</html>
'''
#the filename for the HTML file to be created
filename = "oower.html"

#write the HTML contents to a file
strToFile(contents, filename)

#open the HTML file in the default browser
webbrowser.open("file:///" + os.path.abspath(filename))
