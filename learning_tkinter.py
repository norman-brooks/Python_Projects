
import tkinter
from tkinter import *

# Parent class

class ParentWindow(Frame):
    def __init__ (self, master):
        # below we set up the frame
        # You would also put **args and **kargs in the function above(argument, keyword argument)
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False) # This will keep the new window from being resized
        self.master.geometry('{}x{}'.format(700, 400)) 
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        self.varFName = StringVar()
        self.varLName = StringVar()

        # Below we're invoking labels to put on the boxes to help the user

        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblFName.grid(row=0, column=0, padx=(30, 0), pady=(30, 0)) # we add padx & pady to give space in the cell itself. two numbers-first is for the left, second for the right

        self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblLName.grid(row=1, column=0, padx=(30, 0), pady=(30, 0) ) # x is horizontal, y is vertical

        # Below is the label for the buttons

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblDisplay.grid(row=3, column=1, padx=(30, 0), pady=(30, 0))

        # The code below "paints" the text we've called upon. 

        self.txtFName = Entry (self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue' )# widgets we're calling from Tkinter
        self.txtFName.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))

        self.txtLName = Entry (self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue' )# widgets we're calling from Tkinter
        self.txtLName.grid(row=1, column=1, padx=(30, 0), pady=(30, 0)) # pack is one of the placement managers. We've changed it and turned it into grid on video 3

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit) # you can change the button size itself
        self.btnSubmit.grid(row=2, column=1, padx=(0, 0), pady=(30, 0), sticky=NE) # We've added a submit button. Sticky uses directions (N, S, E, W)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel) # we put the command function on both buttons
        self.btnCancel.grid(row=2, column=1, padx=(0, 90), pady=(30, 0), sticky=NE)

    # Below are the functions to make the buttons operational

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn, ln)) # Whenever you change something you need to use config (configure)

    def cancel(self):
        self.master.destroy() # destroy is the command to close the window
        

        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    # Below is the most important line. If you don't do mainloop() it won't continue to run
    root.mainloop()
