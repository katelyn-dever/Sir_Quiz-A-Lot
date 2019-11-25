# Sir Quiz-A-Lot desktop application
# I didn't delete any previous work, I just couldn't use "input" and things like that with the GUI
# It's all at the bottom commented out.
# Since we aren't using version control, try to comment out my code instead of deleting..
# we can clean it up later.
# Was also thinking about finding a way to put all of the repetitive code like padx pady font and color into variables or
# a function so that it wont be so repetitive. That can be a stretch goal. - K

import math
import random
# used for GUI
from tkinter import *

root = Tk()

###FUNCTIONS###
#global dictionary?  is this dangerous?
terms = dict()

def addTerm():
    terms.update({termEntry.get():defEntry.get()})
    termEntry.delete(0, END)
    defEntry.delete(0, END)
    

def QuizA():
    QuizAWindow = Toplevel()
    QuizAWindow.title("Quiz Using Terms/Questions")
    QuizAWindow.iconbitmap('C:/python/sqal/sqal.ico')

    # used for random int
    num = len(terms)-1

    #counter for rows
    i = 1

    key_list = list(terms.keys())
    val_list = list(terms.values())
    
    def generate():
        x = random.randint(0, num)
        k = StringVar()
        k.set(key_list[x])
        v = StringVar()
        v.set(val_list[x])
        l = Label(QuizAWindow, textvariable=k)
        l.grid(row=1, column=1, pady=20, padx=20)

        def reveal(v):
            l.config(textvariable=v)

        revealButton = Button(QuizAWindow, text="Reveal", command= lambda: reveal(v))
        revealButton.grid(row=2,column=1, columnspan=1,padx=10,pady=10)

    generate()

    nextButton = Button(QuizAWindow, text="Next", command=generate)
    nextButton.grid(row=2, column=2, columnspan=1, padx=10, pady=10)
    
    closeButton = Button(QuizAWindow, text="Close",command=QuizAWindow.destroy)
    closeButton.grid(row=3,column=2,columnspan=1,padx=10,pady=10)

def QuizB():
    QuizBWindow = Toplevel()
    QuizBWindow.title("Quiz Using Terms/Questions")
    QuizBWindow.iconbitmap('C:/python/sqal/sqal.ico')

    # used for random int
    num = len(terms)-1

    #counter for rows
    i = 1

    key_list = list(terms.keys())
    val_list = list(terms.values())
    
    def generate():
        x = random.randint(0, num)
        k = StringVar()
        k.set(key_list[x])
        v = StringVar()
        v.set(val_list[x])
        l = Label(QuizBWindow, textvariable=v)
        l.grid(row=1, column=1, pady=20, padx=20)

        def reveal(k):
            l.config(textvariable=k)

        revealButton = Button(QuizBWindow, text="Reveal", command= lambda: reveal(k))
        revealButton.grid(row=2,column=1, columnspan=1,padx=10,pady=10)

    generate()

    nextButton = Button(QuizBWindow, text="Next", command=generate)
    nextButton.grid(row=2, column=2, columnspan=1, padx=10, pady=10)
    
    closeButton = Button(QuizBWindow, text="Close",command=QuizBWindow.destroy)
    closeButton.grid(row=3,column=2,columnspan=1,padx=10,pady=10)

def showAll():
    
    showAllWindow = Toplevel()
    showAllWindow.title("All Terms Entered")
    showAllWindow.iconbitmap('C:/python/sqal/sqal.ico')

    #counter for rows
    i = 1
    
    for k, v in terms.items():
        stringlist = StringVar()
        stringlist.set(k + " : " + v)
        l = Label(showAllWindow, textvariable=stringlist)
        l.grid(row=i, column = 1, pady=20, padx=50)
        i= i+1
        
    closeButton = Button(showAllWindow, text="Close",command=showAllWindow.destroy)
    closeButton.grid(row=i,column=2,columnspan=1,padx=10,pady=10)
        

def rootExit():
	#prompts to save upon closing (once save feature added, until then it just warns user to save first)
	closeWindow = Toplevel()
	closeWindow.title("*Unsaved Changes*")
	closeWindow.iconbitmap('C:/python/sqal/sqal.ico')
	exitLabel = Label(closeWindow, text="Are you sure you want to exit? Please make sure to save all changes.")
	exitLabel.grid(row=0,column=0,columnspan=3,pady=20,padx=20)
	exitButtonFinal = Button(closeWindow, text="Exit",command=root.destroy)
	exitButtonFinal.grid(row=2,column=3,columnspan=1,pady=10,padx=10)
	backToProgramButton = Button(closeWindow, text="Go back to my quiz",command=closeWindow.destroy)
	backToProgramButton.grid(row=2,column=2,columnspan=1,pady=10,padx=10)


###BEGIN GUI BUILD###

#Window creation and overall styles

root.title("Sir Quiz-A-Lot")
root.iconbitmap('C:/python/sqal/sqal.ico')


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
introLabel = Label(root,
                   text = "Hello!  Welcome to Sir Quiz-A-Lot!",
                   pady = 20,
                   padx = 100)
introLabel.grid(row = 0, columnspan = 5)

#intro paragraph text
detailsLabel = Label(root,
                     text = """Enter as many term/definition or question/answer pairs as you wish, \nthen use the buttons below to quiz yourself!""",
                     pady = 20,
                     padx = 100)
detailsLabel.grid(row = 1, columnspan = 5)

#term label and entry
termLabel = Label(root,
                  text = "Enter a term/question: ",
                  pady = 20)
termLabel.grid(row = 2, column = 0)
termEntry = Entry(root,
                  width = 75)
termEntry.grid(row = 2, column = 1,
               padx = 20, pady = 20,
               columnspan = 4)


#definition label and entry
defLabel = Label(root,
                 text = "Enter its definition/answer: ",
                 padx = 20,
                 pady = 20)
defLabel.grid(row = 3, column = 0)
defEntry = Entry(root,
                 width = 75)
defEntry.grid(row = 3, column = 1,
              padx = 20, pady = 20,
              columnspan = 4)



#Add to quiz button
addToQuizButton = Button(root,
                         text = "Add to Quiz",
                         padx = 10, pady = 10,
                         command=addTerm)
addToQuizButton.grid(row = 4, columnspan = 3, column = 1)

#Quiz me using Terms button
quizTermsButton = Button(root,
                         text = "Quiz me using Terms/Questions",
                         padx = 10, pady = 10,
                         command=QuizA)
quizTermsButton.grid(row = 5, columnspan = 3, column = 1)

#Quiz me using Defintions button
quizDefsButton = Button(root,
                        text = "Quiz Me using Definitions/Answers",
                        padx = 10, pady = 10,
                        command=QuizB)
quizDefsButton.grid(row = 6, columnspan = 3, column = 1)

#Show All Entries button
showAllButton = Button(root,
                       text = "Show All Quiz Entries",
                       padx = 10, pady = 10,
                       command=showAll)
showAllButton.grid(row = 7, columnspan = 3, column = 1)

#Exit button
exitButton = Button(root,
                       text = "Exit",
                       padx = 10, pady = 10,
                       command=rootExit)
exitButton.grid(row = 8, columnspan = 3, column = 1)



    

    
    
    




root.mainloop()
