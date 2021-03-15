from tkinter import *

w = Tk()
e = Entry(w, width=50, bg="tomato", borderwidth=0 )
e.pack()
e.insert(5, "type something here...")

def click():
    lab1 = Label(w, text=e.get())
    lab1.pack()

# button widgets
b1 = Button(w, text="Release the Kraken!", command=click)
# b2 = Button(w, text="Done", padx=30, command=exit, fg="#ff22aa", bg="black")
b2 = Button(w, text="Done", padx=30, command=exit)


b1.pack()
b2.pack()

# run the loop
w.mainloop()