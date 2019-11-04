# Sir Quiz-A-Lot desktop application
# I didn't delete any previous work, I just couldn't use "input" and things like that with the GUI
# It's all at the bottom commented out.
# Since we aren't using version control, try to comment out my code instead of deleting..
# we can clean it up later.
# Was also thinking about finding a way to put all of the repetitive code like padx pady font and color into variables or
# a function so that it wont be so repetitive. That can be a stretch goal. - K

import math
# used for GUI
import tkinter as tk
# used to change fonts
import tkinter.font as tkFont
# used to make entry text boxes larger
from tkinter.scrolledtext import ScrolledText

#global dictionary?  is this dangerous?
terms = {}

def addTerm(x, y):
    #doesnt work yet
    terms[x] = y

def QuizA():
    return

def QuizB():
    return

def showAll():
    #currently functioning but only in shell, will eventually have its own GUI in a new window
    print(terms)

def main():
    

    ###BEGIN GUI BUILD###

    #Window creation and overall styles
    root= tk.Tk()
    root.title("Sir Quiz-A-Lot")
    # width x height + x_offset + y_offset
    root.geometry("800x800+30+30")
    myFont = tkFont.Font(family="verdana", size = 14)
    titleFont = tkFont.Font(family = "verdana", size = 20)
    frame = tk.Frame(root)

    ## ATTEMPT at making a file toolbar to save and open files.  doesn't work yet
    #menu bar
    #menu = Menu(root)
    #root.config(menu=menu)
    #subMenu = Menu(menu)
    #menu.add_cascade(label="File", menu=subMenu)
    #subMenu.add_command(label="New Project...", command=doNothing)
    #subMenu.add_command(label="Save", command = doNothing)
    #subMenu.add_separator()
    

    #title at top of GUI     
    tk.Label(root,
            text = "Hello!  Welcome to Sir Quiz-A-Lot!",
            pady = 20,
            padx = 50,
            font = titleFont,
            fg = "black").grid(row = 0, columnspan = 5)
    
    #intro paragraph text
    tk.Label(root,
            text = """Enter as many term/definition or question/answer pairs as you wish, \nthen use the buttons below to quiz yourself!""",
            pady = 20,
            padx = 50,
            font = myFont,
            fg = "black").grid(row = 1, columnspan = 5)

    #term entry
    term_w = 30
    term_h = 2
    tk.Label(root,
             text = "Enter a term/question: ",
             pady = 20,
             font = myFont,
             fg = "black").grid(row = 2, column = 0)
    term = ScrolledText(root, width = term_w, height = term_h, wrap = tk.WORD).grid(row = 2, column = 1)

    #definition entry
    def_w = 30
    def_h = 5
    tk.Label(root,
             text = "Enter its definition/answer: ",
             padx = 20,
             pady = 20,
             font = myFont,
             fg = "black").grid(row = 3, column = 0)
    definition = ScrolledText(root, width = def_w, height = def_h, wrap = tk.WORD).grid(row = 3, column = 1)

    #Add to quiz button
    addToQuizButton = tk.Button(root,
                                text = "Add to Quiz",
                                font = myFont,
                                fg = "black",
                                command=addTerm(term, definition)).grid(row = 4, column = 1)

    #Quiz me using Terms button
    tk.Button(root,
              text = "Quiz me using Terms/Questions",
              font = myFont,
              fg = "black",
              command=QuizA).grid(row = 5, column = 1)

    #Quiz me using Defintions button
    tk.Button(root,
              text = "Quiz Me using Definitions/Answers",
              font = myFont,
              fg = "black",
              command=QuizB).grid(row = 6, column = 1)
    
    #Show All Entries button
    tk.Button(root,
              text = "Show All Quiz Entries",
              font = myFont,
              fg = "black",
              command=showAll).grid(row = 7, column = 1)
    
    root.mainloop()

# This will be the number of terms to define.
# Do we really need to specify the number? what if they want to add a term later?

    ## probably delete: termNum = eval(input("Please enter the total number of terms you want to input for this session: "))

# Here is the loop that accepts and stores terms

#def termInput():
    #terms = {}
    ## if termNum > 0 and termNum == int:
    #index = -1
    #while index < 0:
       # terms[input("Enter the next term:")] = input("Now enter the matching definition:")
        #index + 1
        #cont = eval(input("Would you like to enter another term? Enter 'y' for yes or 'n' for no."))
        #if str(cont) is 'n':
          #  break
       # else:
            #continue

                    
#print(terms.items())            
            
                         
## terms.append(input("Please enter a term:"))
            ## terms.sort(key=
    
            
  ## else:
       ## print("Please enter a positive integer.")

main()
