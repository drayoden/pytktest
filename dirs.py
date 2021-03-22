from tkinter import *
from tkinter import filedialog

w = Tk()
w.title("Folders")

r = filedialog.askdirectory(initialdir="/home/sysadm", title="Select directory")

label = Label(w, text=r).pack()

btn_exit = Button(w, text="Exit", command=w.quit)
btn_exit.pack()



w.mainloop()