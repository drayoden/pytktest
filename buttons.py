from tkinter import *

w = Tk()

def click():
    lab1 = Label(w, text="Clicked!")
    lab1.pack()

# button widgets
b1 = Button(w, text="Release the Kraken!", command=click)
b2 = Button(w, text="Ok", padx=30, command=exit, fg="#ff22aa", bg="black")


b1.pack()
b2.pack()

# run the loop
w.mainloop()