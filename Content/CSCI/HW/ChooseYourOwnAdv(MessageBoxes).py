import tkinter as tk
from tkinter import *
import random
import math
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.scrolledtext as tkst


                                                ## Starting Window
                  ## global variables
global window, can_height, can_width, my_can, wrong,x , name

## Count the number of incorrect answers for the two games/problems
wrong = 0
x = 0
                  ## Create APP Window
window = tk.Tk()
window.title('Choose Your Own Adventure')

cv = tk.Canvas(window, width=600, height=502)
cv.pack()

name = simpledialog.askstring("Input", "Enter your name:", parent=window)
    ## add canvas text at coordinates x=15, y=20
    ## anchor='nw' implies upper left corner coordinates(northwest)
Title = cv.create_text(15, 20, text="Welcome..."+ str(name) + "! Let's begin the story. \n Are you ready?", font = ("Impact", 30), fill="#ff0000", anchor='nw' )

cv.create_text(100, 210, text= "Aokigahara", font = ("Impact", 100), fill= "#ff0000", anchor = "nw")


                                          ##Game/Story Code begins
class SolveMath: ## random ## math
##      def __init__(self):
##            global window
##            global my_can
##            global can_height
##            global can_width
##            global wrong
##            wrong = 0
##
##            self.w = can_width
##            self.h = can_height
##
### create application window and canvas
##            window = tk.Tk()
##            window.title("Math and Pass")
##
##            title = tk.Label(window, text = "Math and Pass")
##            title.pack()
##            title.config(font = ("impact", 40))
##            #global window
##                  ## HOW TO CLEAR CANVAS 
##            #window.grid_forget()
##                  ## Change the title after (without making a new window)
##            #window.itemconfig(title = "Math and pass")
##            M_can = tk.Canvas(window, width = self.w, height = self.h)
##            M_can.pack()

      ## Math mathematical questions (to solve)
      ## ask true or false / multiple choice?
      def addition():
            global wrong
            a = random.randrange(0,999)
            b = random.randrange(0,999)
            A = int(a + b)
            
                        ## HOW TO MAKE IT APPEAR ON THE CANVAS/WIN
            user_input = int(input("what is" + str(a) + "+" + str(b) + "?"))
            AdditionL = tk.Label(window,text= user_input)
            AdditionL.pack()
            if user_input == A:
                  print ("woot")
            else:
                  wrong +=1

      def subtraction():
            global wrong
            a = random.randrange(0,999)
            b = random.randrange(0,999)
            answer = a - b
                        ## HOW TO MAKE IT APPEAR ON THE CANVAS/WIN
            user_input = int(input("what is" + str(a) + "-" + str(b) + "?"))
            SubtractionL = tk.Label(window, text = user_input)
            SubtractionL.pack()
            if user_input == answer:
                  print ("Good Job")
            else:
                  wrong +=1
                  
      def square ():
            global wrong
            a = int(random.randrange (0, 11))
            b = int(random.randrange (0, 11))
            c = int(random.randrange (0, 11))
            d = int(random.randrange (0, 11)) 
            SQanswer = c**d
            SRanswer = int(math.sqrt(a))+ int(math.sqrt(b))
            num = random.randrange(0,2)
            if num == 0:
                  user_input = int(input("what is " + str(c) + " to the power of " + str(d) +"?"))
                  if user_input == SQanswer:
                        print ("Great Job!")
                  else:
                        wrong +=1
            else:
                  user_input = int(input(("what is the square root of " + str(a) + " plus the square root of " + str(b)+"?")))
                  if user_input == SRanswer:
                        print ("insert positive message?")
                  else:
                        wrong +=1
      def divMul ():
            global wrong
                        ## getting random number within the range
            a = int(random.randrange (0, 11))
            b = int(random.randrange (1, 11))
            c = int(random.randrange (0, 50))
            d = int(random.randrange (0, 50))
            divanswer = a//b
            Mulanswer = c*d
                        ## random coin toss to decide if you'll be asked a division or multiplication problem
            num = random.randrange(0,2)
            if num == 0:
                  user_input = int(input("what is " + str(a) + " divided " + str(b) + " (integer form)?"))
                  if user_input == divanswer:
                        print ("another positive mess.")
                  else:
                        wrong +=1
            else:
                  user_input = int(input(("what is " + str(c) + " * " + str(d)+"?")))
                  if user_input == Mulanswer:
                        print ("great, you still have ways to go")
                  else:
                        wrong +=1
                              ## ADD TRY/ EXCEPT for the ZeroDivisonError
            

            
                              ## randomly choose which function/question to ask the user
      def chooseRan ():
            for i in range (5):
                  opt = ["addition", "subtraction", "square","divMul"]
                  selected = random.choice(opt)
                  if selected == "addition":
                        SolveMath.addition()
                  elif selected == "subtraction":
                       SolveMath.subtraction()
                  elif selected == "square":
                        SolveMath.square()
                  else:
                        SolveMath.divMul()


                  ## Riddle Class
class Riddle:
##      def __init__(self):
##            global window
##            global my_can
##            global can_height
##            global can_width
##            global x
##            x = 0
##
##            self.w = can_width
##            self.h = can_height
##
##            # create application window and canvas
##            window = tk.Tk()
##            window.title("Riddle")
##
##            title = tk.Label(window, text = "Riddle")
##            title.pack()
##            title.config(font = ("impact", 40))
##            #global window
##            ## HOW TO CLEAR CANVAS 
##            #window.grid_forget()
##            ## Change the title after (without making a new window)
##            #window.itemconfig(title = "Math and pass")
##            R_can = tk.Canvas(window, width = self.w, height = self.h)
##            R_can.pack()

      def rid0 ():
            global x
            global window
            # What disappears as soon as you say its name?
            answer0 = "silence"
            user_input = simpledialog.askstring("", "What disappears as soon as you say its name?", parent=window)
            if user_input == answer0:
                print ("ure such a smart cookie")
            else:
                print ("nIcE tRy dUde")
                x+=1
                
                  
            
      def rid1 ():
            global x
            global window
            # I’m tall when I’m young and short when I’m old. What am I?
            answer1 = "a candle"
            user_input = simpledialog.askstring("", "I'm tall when I'm young and short when I'm old. What am I?", parent=window)
            if user_input == answer1:
                print ("You got it!")
            else:
                print ("Sorry bruh, next time.")
                x+=1


            #rid2_label = tk.Label(H_win, text = user_input)
            
      def rid2 ():
            global x
            global window
            # What can you hold in your right hand, but never in your left hand?
            answer2 = "your left hand"
            user_input = simpledialog.askstring("", "What can you hold in your right hand, but never in your left hand?", parent=window)
            if user_input == answer2:
                print ("Yass")
            else:
                print ("You thought...")
                x+=1

            
            #H_can.draw_line(25,10,50,10, color = "black")
      def rid3 ():
            global x
            global window
            #Write cow in 13 letters.
            answer3 = "see o double you"
            user_input = simpledialog.askstring("", "Write cow in 13 letters", parent=window)
            if user_input == answer3:
                print ("Gud job")
            else:
                print ("Moo-ve out of the way, you're wrong")
                x+=1


            
      def rid4 ():
            global x
            global window
            #What can travel around the world while staying in a corner?
            answer4 = "a stamp"
            user_input = simpledialog.askstring("", "What can travel aound the world while staying in the corner?", parent=window)
            if user_input == answer4:
                print ("Look at you, so smart")
            else:
                print ("Read that again, yo")
                x+=1

      def rid5 ():
            global x
            global window
            #What can travel around the world while staying in a corner?
            answer5 = "there is no missing dollar"
            messagebox.showinfo("Part 1","Three people check into a hotel room.")
            messagebox.showinfo("Part 2","The manager says the bill is $30, so each guest pays $10. Later the manager realizes the bill should only be $25")
            messagebox.showinfo("Part 3", '''To fix this, he gives the bellhop 5 single bills to return to the guests. On the way to the room, the bellhop realizes that he cannot divide the money equally,and decides to give each guest $1 and keep $2 as a tip for himself''')
            messagebox.showinfo("Part 4", "Each guest gets $1 back, so now each guest has paid $9. This brings the total paid amount to $27, and the bellhop has $2")
            user_input = simpledialog.askstring("", "$27 + $2 = $29. But the guests originally paid $30. What happened to the missing dollar?", parent=window)
            if user_input == answer5:
                print ("")
            else:
                print ("")
                x+=1


                  #Three people check into a hotel room. The manager says the bill is $30,
                  #so each guest pays $10. Later the manager realizes the bill should only
                  #be $25. To fix this, he gives the bellhop 5 single bills to return to the guests.
                  #On the way to the room, the bellhop realizes that he cannot divide the money equally,
                  #and decides to give each guest $1 and keep $2 as a tip for himself. Each guest gets $1 back,
                  #so now each guest has paid $9. This brings the total paid amount to $27, and the bellhop has $2. 

                  #$27 + $2 = $29. But the guests originally paid $30. What happened to the missing dollar? 
                
            ## Choose randomly which math problems one will solve
      def Chosen_riddle():
            global x
            for i in range (5):
                  Catlist = [0,1,2,3,4]
                  selected = random.choice(Catlist)
                  if selected == 0:
                        Riddle.rid0()
                  elif selected == 1:
                        Riddle.rid1()
                  elif selected == 2:
                        Riddle.rid2()
                  elif selected == 3:
                        Riddle.rid3()
                  else: 
                        Riddle.rid4()
            Riddle.rid5()
            

            if x >3:
                  ## Answer wrong too many times and the story ends
                  End = messagebox.showwarning("Warning! ", "You got what you wanted! I mean, this is why you came here, right?")
                  if End == True:
                        window.destroy()

                  
                  

def info ():
     messagebox.showinfo("Information", "This is important information made by Chamee and Lissie. Yes, that is all. ")
     messagebox.askokcancel("Now what", "Is it time to return...")
     name = simpledialog.askstring("Just checking", "Positive:", parent=window)

def CompassorNot():
      Text6 = messagebox.askyesno("Now what", '''So, I see you came prepared. You brought a bottle of water,
      a compass, and a knife. First off, you can get rid of your compass, as it won’t work here.
      The iron in this soil makes it useless.''')
      Text6 = messagebox.askyesno( "ask", '''Do you want to toss the compass?''')
      print (Text6)
      if Text6 == True:
            text6 = messagebox.askokcancel("Toss","Nice choice, you don’t need the dead weight.")
      else:
            messagebox.askokcancel("Keep", '''Great, you’re gonna carry around something that’s useless while
            you’re in a place filled with corpses and haunted by ghosts. Smart.''')
def KnifeorNot():
      global name
      Text7 = messagebox.askyesno("Now what?", '''Now, about that knife. It’s preeeettty dull, don’t you think? \nThere’s plenty of skeletons
                  out here with knives attached to their hands. Wanna try your luck and \n toss out that knife in hopes of picking up a better one?''')
      if Text7 == True:
            text7 = messagebox.askokcancel("Toss", "You remember I told you some things are not what they seem, right? But, I respect your decision " + name)
##            text7 = tk.Label(window, "You remember I told you some things are not what they seem, right? But, I respect your decision " + name)
##            text7.place(x =300,y = 300)
      if Text7 == "No":
            noText7 = messagebox.askokcancel("Keep", " I'm admit, I have been wrong before")
##            noText7 =tk.Label(window, "Okay. I’ll admit, I have been wrong before")
##            noText7.place(x = 300, y = 300, anchor = "sw")

def MathChallenge ():
      challenge = messagebox.askyesno("Now what?", '''Now, about that knife. It’s preeeettty dull, don’t you think? \nThere’s plenty of skeletons
                  out here with knives attached to their hands. Wanna try your luck and \n toss out that knife in hopes of picking up a better one?''')
      if challenge == "True":
            SolveMath.chooseRan()
      else:
            noText7 = messagebox.askokcancel("...", " That's too bad, you already walked into it.")
            SolveMath.chooseRan()



## Storyboard

def Storycont():
      CompassorNot()
      KnifeorNot()
                        ## The story pops up in the messageboxes
      messagebox.showinfo(" ","Let’s start walking!" )
      messagebox.showinfo(" ","Hey!")
      messagebox.showinfo(" ", "Watch where you’re stepping!")
      messagebox.showinfo(" ","My good man Al is right underneath your feet!")
      messagebox.showinfo(" ","He came to this place 20 years ago, a scared college student who feared that he was going to school for his parents and not for himself!")
      messagebox.showinfo(" ","What a shame. He was such a good math student. *sigh*")
      messagebox.showinfo(" ", "Look what you’ve done. Al is not a fan of people who step all over him, literally and figuratively!! Now you have to face your consequence…")
      messagebox.showwarning("Warning! ", "Everyone’s worst fear…")
      messagebox.showinfo(" ", "MATH!!")
      Response = messagebox.askyesno("Challenge", "Do you accept?")
                        ## if the user selects yes or no it will bring them to the math game
      if Response == True:
            SolveMath.chooseRan()
                        ## if the user enters 4 wrong answers the story will end or else the story will continue
            if wrong > 3:
                  End = messagebox.showwarning("Warning! ", "The END")
                  if End == True:
                        window.destroy()
            else:
                  messagebox.showinfo(" ","Whew, you made it with some life to spare. You’re lucky Al is a nice guy. HEY! What did I tell you about watching where you step?!")
                  messagebox.showinfo(" ","You’ve done it now. You inconsiderate humans never show any respect! Why do I bother to help any of you?!")
                  messagebox.showinfo(" ","Where are your manners?")
                  messagebox.showinfo(" ", "Say hi to the next person you stepped on, (woman's name)")
                  messagebox.showinfo(" ", "Her children left her for the city, and after her husband died, she couldn’t bear the loneliness anymore.")
                  BeginRid = messagebox.showinfo(" ", " (woman's name): Hello child, answer these riddles correctly and I will contemplate letting you pass...")
                  print(BeginRid)
                  if BeginRid == "ok":
                        Riddle.Chosen_riddle()
                        if x > 3:
                              End = messagebox.showwarning("THE END ", "You got what you wanted! I mean, this is why you came here, right?")
                              if End == True:
                                    window.destroy()
                        else:
                              messagebox.showinfo("YOU LIVE","So, you didn’t die. Sorry if that’s what you wanted. You’ll have to try harder next time.")                 
      else:
            SolveMath.chooseRan()
            if wrong > 3:
                  End = messagebox.showwarning("Warning! ", "The END")
                  if End == True:
                        window.destroy()
            else:
                  messagebox.showinfo(" ","Whew, you made it with some life to spare. You’re lucky Al is a nice guy. HEY! What did I tell you about watching where you step?!")
                  messagebox.showinfo(" ","You’ve done it now. You inconsiderate humans never show any respect! Why do I bother to help any of you?!")
                  messagebox.showinfo(" ","Where are your manners?")
                  messagebox.showinfo(" ", "Say hi to the next person you stepped on, (woman's name)")
                  messagebox.showinfo(" ", "Her children left her for the city, and after her husband died, she couldn’t bear the loneliness anymore.")
                  BeginRid = messagebox.showinfo(" ", " (woman's name): Hello child, answer these riddles correctly and I will contemplate letting you pass...")
                  print(BeginRid)
                  if BeginRid == "ok":
                        Riddle.Chosen_riddle()
                        if x > 3:
                              End = messagebox.showwarning("THE END! ", "You got what you wanted! I mean, this is why you came here, right?")
                              if End == True:
                                    window.destroy()
                        else:
                              messagebox.showinfo(" YOU LIVE ","So, you didn’t die. Sorry if that’s what you wanted. You’ll have to try harder next time.")             

      
def Main ():
      global wrong, window
##
      canv =tk.Canvas(window, width = 688, height = 502)
      canv.pack()

                        ## Create a scrollbar for window
##      scrollbar=Scrollbar(window)
##      scrollbar.pack(side = LEFT, fill = Y)
                  ## Scroll Text(???)
##      frame1 = tk.Frame(master = canv, bg = '#3d291f')
##      frame1.pack(fill = 'both', expand = 'no')
##      editArea = tkst.ScrolledText(master = canv, wrap = tk.WORD, width = 80, height = 30)
##      editArea.pack(padx = 10, pady = 10, fill = tk.BOTH, expand = False)


      messagebox.showinfo(" ", "Be careful. Or don’t be. You are in Aokigahara, the \n suicide forest. \n So, let’s begin, hmm?")
      messagebox.showinfo(" ", "You’ve arrived. Welcome to “the sea of trees,” “the perfect place to die,” or so I hear from the humans who visit this place. Here, you will see things that aren’t really there, for nothing is ever as it seems.") 
      Response = messagebox.askyesno("First, choose your path. \n No pressure--you’re just deciding your fate from here on out.", "Do you want to go left (Y) or right(N)?")
      if Response == "True":
            messagebox.askokcancel("Now what", "So you made your choice. Are you sure you’re ready?")
            messagebox.showinfo(" ", "Lets begin...")
            SolveMath.hooseRan()
            if wrong > 3:
                  End = messagebox.showwarning("Warning! ", "The END")
                  if End == True:
                        window.destroy()
            else:
                  Storycont()
      else:
            messagebox.askokcancel("Now what", "So you made your choice. Are you sure you’re ready?")
            messagebox.showinfo(" ", "Lets begin...")
            SolveMath.chooseRan()
            if wrong > 3:
                  End = messagebox.showwarning("Warning! ", "The END")
                  if End == True:
                        window.destroy()
            else:
                  Storycont()

      

      ## Story Begins Window

##      quit_button2 = tk.Button(window, text = "Quit")
##      quit_button2.place(x = 300, y = 430)
##      quit_button2['command'] = window.destroy


                       


## Starting Window
start_button = tk.Button (window, text = "Begin Story")
start_button.place(x = 100, y = 430)
start_button['command'] = Main

info_button = tk.Button(window, text = "Information")
info_button.place(x = 200, y = 430)
info_button['command'] = info

quit_button = tk.Button(window, text = "Quit")
quit_button.place(x = 300, y = 430)
quit_button['command'] = window.destroy







## once the game/story begins
##restart_button = tk.Button (main_win, text = "Restart Game")
##restart_button.place(x = 250, y = 450, anchor = "center")
##restart_button['command'] = Main



window.mainloop()

## https://runestone.academy/runestone/static/CS121/
## GUIandEventDrivenProgramming/07_event_binding.html
