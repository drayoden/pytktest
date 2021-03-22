from tkinter import *
from PIL import ImageTk, Image

w = Tk()
w.title("Images")

# LAME * SUCKS * LAME * SUCKS * LAME * SUCKS * LAME * SUCKS
# apparently using a favicon or bitmap for
# the upper left of the app is a non-starter for 
# linux because of the X-windows system, 
# linux will only understand .xbm files 
# which are lame and sad, this does not
# work:
#       w.iconbitmap("Games-16x16.png")

# trying this instead, found on stackoverflow:
# PhotoImage is included in tkinter
# successfully launched with png file but did not display it. 
# Errored with an ico file; did not recognize it.
#       w.iconphoto(True, PhotoImage(file="troll.png")) 
# LAME * SUCKS * LAME * SUCKS * LAME * SUCKS * LAME * SUCKS

img = ImageTk.PhotoImage(Image.open("troll.png"))
label = Label(image=img)
label.pack()

btn_exit = Button(w, text="Exit", command=w.quit)
btn_exit.pack()



w.mainloop()