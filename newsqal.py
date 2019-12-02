### Sir Quiz-A-Lot desktop application ###
### ITEC 3250 - Katelyn Dever, Elijah Cliett, Brianna Young ###


### Imports ###
import math
import random
# used for GUI
from tkinter import *
from tkinter import filedialog



### GUI Setup ###
root = Tk()
terms = dict()
windowSize = "750x600"
smWindowSize = "400x400"
xsWindowSize = "100x100"

print("Program running, no errors on load")



### FUNCTIONS ###
def updateCount():
    countVar = StringVar()
    countVar.set(str(len(terms)))
    #counter label
    counterLabel = Label (root,
                          text = "Number of pairs in your quiz:",
                          width = 75,
                          padx = 20,
                          pady = 20)
    counterLabel.grid(row = 4, column = 0, columnspan = 3)
    countLabel = Label(root, textvariable=countVar)
    countLabel.grid(row = 4, column = 2)
    
    
def openFile():
    root.filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select file",
                                              filetypes = (("txt files", "*.txt"), ("all files", "*.*")))
    f = open(root.filename, "r")
    
    for line in f:
        (key, val) = line.split()
        terms[key] = val

    updateCount()
    
def saveFile():
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",
                                                  title = "Select file",
                                                  filetypes = (("txt files","*.txt"),("all files","*.*")))

    i = 1
    f = open(root.filename, "w")
    
    for k, v in terms.items():
        f.write("%s %s\n" %(k, v))

def addTerm():
    if len(termEntry.get()) != 0:
        if len(defEntry.get()) !=0:
            terms.update({termEntry.get():defEntry.get()})
            termEntry.delete(0, END)
            defEntry.delete(0, END)
            updateCount()
        else:
            errorWindow = Toplevel()
            errorWindow.title("Error")
            errorWindow.iconbitmap('C:/python/sqal/sqal.ico')
            errorLabel = Label(errorWindow, text = "Invalid Definition Entry")
            errorLabel.pack()
            okButton = Button(errorWindow, text = "Okay", command=errorWindow.destroy)
            okButton.pack()
    else:
        errorWindow = Toplevel()
        errorWindow.title("Error")
        errorWindow.iconbitmap('C:/python/sqal/sqal.ico')
        errorLabel = Label(errorWindow, text = "Invalid Term Entry")
        errorLabel.pack()
        okButton = Button(errorWindow, text = "Okay", command=errorWindow.destroy)
        okButton.pack()
    

def QuizA():
    if len(terms) >=3:
        # creates new window
        QuizAWindow = Toplevel()
        QuizAWindow.title("Quiz Using Terms/Questions")
        QuizAWindow.iconbitmap('C:/python/sqal/sqal.ico')
        QuizAWindow.geometry(smWindowSize)

        # used for random int
        num = len(terms)-1

        key_list = list(terms.keys())
        val_list = list(terms.values())

        # creates label to store text variable
        k = StringVar()
        l = Label(QuizAWindow, textvariable=k)
        l.grid(row=1, column=1, pady=20, padx=20)
        
        def generate():
            x = random.randint(0, num)
            k.set(key_list[x])

            def reveal():
                k.set(val_list[x])

            revealButton = Button(QuizAWindow, text="Reveal", command=reveal)
            revealButton.grid(row=2,column=1, columnspan=1,padx=10,pady=10)

        # generates first term on open
        generate()

        # on window buttons
        nextButton = Button(QuizAWindow, text="Next", command=generate)
        nextButton.grid(row=2, column=2, columnspan=1, padx=10, pady=10)
        
        closeButton = Button(QuizAWindow, text="Close",command=QuizAWindow.destroy)
        closeButton.grid(row=3,column=2,columnspan=1,padx=10,pady=10)
        
    else:
        errorWindow = Toplevel()
        errorWindow.title("Error")
        errorWindow.iconbitmap('C:/python/sqal/sqal.ico')
        errorLabel = Label(errorWindow, text = "Please enter at least 3 pairs to start a Quiz")
        errorLabel.pack()
        okButton = Button(errorWindow, text = "Okay", command=errorWindow.destroy)
        okButton.pack()

def QuizB():
    if len(terms) >= 3:
        # creates new window
        QuizBWindow = Toplevel()
        QuizBWindow.title("Quiz Using Definitions/Answers")
        QuizBWindow.iconbitmap('C:/python/sqal/sqal.ico')
        QuizBWindow.geometry(smWindowSize)

        # used for random int
        num = len(terms)-1

        key_list = list(terms.keys())
        val_list = list(terms.values())

        # creates label to store text variable
        k = StringVar()
        l = Label(QuizBWindow, textvariable=k)
        l.grid(row=1, column=1, pady=20, padx=20)
        
        def generate():
            x = random.randint(0, num)
            k.set(val_list[x])
            
            def reveal():
                k.set(key_list[x])

            revealButton = Button(QuizBWindow, text="Reveal", command=reveal)
            revealButton.grid(row=2,column=1, columnspan=1,padx=10,pady=10)


        # generates first definition on open
        generate()

        # on window buttons
        nextButton = Button(QuizBWindow, text="Next", command=generate)
        nextButton.grid(row=2, column=2, columnspan=1, padx=10, pady=10)
        
        closeButton = Button(QuizBWindow, text="Close",command=QuizBWindow.destroy)
        closeButton.grid(row=3,column=2,columnspan=1,padx=10,pady=10)
        
    else:
        errorWindow = Toplevel()
        errorWindow.title("Error")
        errorWindow.iconbitmap('C:/python/sqal/sqal.ico')
        errorLabel = Label(errorWindow, text = "Please enter at least 3 pairs to start a Quiz")
        errorLabel.pack()
        okButton = Button(errorWindow, text = "Okay", command=errorWindow.destroy)
        okButton.pack()

def showAll():
    
    showAllWindow = Toplevel()
    showAllWindow.title("All Terms Entered")
    showAllWindow.iconbitmap('C:/python/sqal/sqal.ico')
    showAllWindow.geometry(windowSize)

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

def clearPrompt():
    clearWindow = Toplevel()
    clearWindow.title("Are you sure?")
    clearWindow.iconbitmap('C:/python/sqal/sqal.ico')
    clearLabel = Label(clearWindow, text="Are you sure you want to clear your work?")
    clearLabel.grid(row=0,column=0,columnspan=3,pady=20,padx=20)
    clearButtonFinal = Button(clearWindow, text="Clear",command=clearAll)
    clearButtonFinal.grid(row=2,column=3,pady=10,padx=10)
    backToProgramButton = Button(clearWindow, text="Go back to my Quiz",command=clearWindow.destroy)
    backToProgramButton.grid(row=2,column=2,pady=10,padx=10)

def clearAll():
    terms.clear()
    updateCount()
    

def rootExit():
    #prompts to save upon closing (once save feature added, until then it just warns user to save first)
    closeWindow = Toplevel()
    closeWindow.title("*Unsaved Changes*")
    closeWindow.iconbitmap('C:/python/sqal/sqal.ico')
    exitLabel = Label(closeWindow, text="Are you sure you want to exit? Please make sure to save all changes.")
    exitLabel.grid(row=0,column=0,columnspan=3,pady=20,padx=20)
    exitButtonFinal = Button(closeWindow, text="Exit",command=root.destroy)
    exitButtonFinal.grid(row=2,column=3,pady=10,padx=10)
    backToProgramButton = Button(closeWindow, text="Go back to my Quiz",command=closeWindow.destroy)
    backToProgramButton.grid(row=2,column=2,pady=10,padx=10)


###BEGIN GUI BUILD###

# Window creation and overall styles

root.title("Sir Quiz-A-Lot")
root.iconbitmap('C:/python/sqal/sqal.ico')



# File Menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=openFile)
filemenu.add_command(label="Save Quiz", command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=rootExit)

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
                         width = 30,
                         padx = 20, pady = 20,
                         command=addTerm)
addToQuizButton.grid(row = 0, column = 5)


#Quiz me using Terms button
quizTermsButton = Button(root,
                         text = "Quiz me using Terms/Questions",
                         width = 30,
                         padx = 20, pady = 20,
                         command=QuizA)
quizTermsButton.grid(row = 1, column = 5)

#Quiz me using Defintions button
quizDefsButton = Button(root,
                        text = "Quiz Me using Definitions/Answers",
                        width = 30,
                        padx = 20, pady = 20,
                        command=QuizB)
quizDefsButton.grid(row = 2, column = 5)

#Show All Entries button
showAllButton = Button(root,
                       text = "Show All Quiz Entries",
                       command=showAll,
                       padx = 20, pady = 20,
                       width = 30)
showAllButton.grid(row = 3, column = 5)

#Show All Entries button
clearAllButton = Button(root,
                       text = "Clear All Quiz Entries",
                       command=clearPrompt,
                       padx = 20, pady = 20,
                       width = 30)
clearAllButton.grid(row = 4, column = 5)

#Exit button
exitButton = Button(root,
                    text = "Exit",
                    width = 30,
                    padx = 20, pady = 20,
                    command=rootExit)
exitButton.grid(row = 5, column = 5)



    

    
    
    


updateCount()

root.mainloop()

