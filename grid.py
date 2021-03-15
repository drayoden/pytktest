from tkinter import *

w = Tk()

# label widget
hellolabel1 = Label(w, text="Hello World!").grid(row=0, column=0)
hellolabel2 = Label(w, text="The moosses will be taking control").grid(row=1,column=0)

# hellolabel1.grid(row=1, column=0)
# hellolabel2.grid(row=0, column=0)

# run the loop
w.mainloop()