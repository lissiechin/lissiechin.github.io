## Lissie
## Homework 21
## Due: April 24, 2019

## 1 – Use Tkinter canvas to draw the flag of some country

import tkinter as tk

window = tk.Tk()
my_label = tk.Label(window, text = "flag of France")
my_label.pack()

my_canvas = tk.Canvas(window, width = 300, height = 200)
my_canvas.pack()
my_canvas.create_rectangle(0,0,100,200, fill = "blue")
my_canvas.create_rectangle(200,0,300,200, fill = "red")

quit_button = tk.Button(window, text = "Quit")
quit_button.pack()
quit_button['command'] = window.destroy
window.mainloop()



## 2 – Tkinter w/ 3 buttons on the canvas & draw the flags

nw = tk.Tk()

my_label = tk.Label(nw, text = "FLAGS")
my_label.pack()

def France():
      nw_label = tk.Label(nw, text = "flags: Flag of FRANCE")
      nw_label.pack()

      nw_canvas = tk.Canvas(nw, width = 300, height = 200)
      nw_canvas.pack()
      nw_canvas.create_rectangle(0,0,100,200, fill = "blue")
      nw_canvas.create_rectangle(200,0,300,200, fill = "red")
      
def Belgium ():
      nw_label = tk.Label(nw, text = "flags: Flag of BELGIUM")
      nw_label.pack()
      
      nw_canvas2 = tk.Canvas(nw, width = 300, height = 200)
      nw_canvas2.pack()

      nw_canvas2.create_rectangle(0,0,100,200, fill = "black")
      nw_canvas2.create_rectangle(100,0,200,200, fill = "yellow")
      nw_canvas2.create_rectangle(200,0,300,200, fill = "red")
      

def Indonesia():
      nw_label = tk.Label(nw, text = "flags: Flag of INDONESIA")
      nw_label.pack()

      nw_canvas3 = tk.Canvas(nw, width = 300, height = 200)
      nw_canvas3.pack()
      
      
      nw_canvas3.create_rectangle(0,0, 300,100, fill = "red")

F = tk.Button(nw, text = "France")
F.pack()
F['command'] = France

B = tk.Button(nw, text = "Belgium")
B.pack()
B['command'] = Belgium

I = tk.Button(nw, text = "Indonesia")
I.pack()
I['command'] = Indonesia


quit_button = tk.Button(nw, text = "Quit")
quit_button.pack()
quit_button['command'] = nw.destroy
nw.mainloop()



## 3 – randomly sized circles and fill color randomly

import random

cirWin = tk.Tk()
my_label = tk.Label(cirWin, text = "Random Circles")
my_label.pack()

cirWin_canvas = tk.Canvas(cirWin, width = 300, height = 300)
cirWin_canvas.pack()

def randcirc ():
      fSet = random.randrange (0,301)
      sSet = random.randrange (0, 301)

      r = random.randrange(0,255)
      g = random.randrange(0,255)
      b = random.randrange(0,255)
      color = "#{:02x}{:02x}{:02x}".format(r,g,b)

      cirWin_canvas.create_oval(fSet, sSet,sSet, fSet, fill = color)

DrawC = tk.Button(cirWin, text = "Draw a Circle")
DrawC.pack()
DrawC['command'] = randcirc
      
quit_button = tk.Button(cirWin, text = "Quit")
quit_button.pack()
quit_button['command'] = cirWin.destroy
cirWin.mainloop()


