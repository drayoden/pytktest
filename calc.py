from tkinter import *

w = Tk() 
w.title("Calc")

e = Entry(w, font=("Calibri",30), width=10, borderwidth=0, justify="right" )
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(n):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(n) )

def button_clear():
    e.delete(0, END)

def button_add():
    first = e.get()
    global g_fnum 
    global math
    math = "+"
    g_fnum = int(first) 
    e.delete(0, END)

def button_equal():
    second = int(e.get())
    e.delete(0, END)
    if math == '+':
        e.insert(0, g_fnum + second)    
    if math == '-':
        e.insert(0, g_fnum - second)    
    if math == '*':
        e.insert(0, g_fnum * second)    
    if math == '/':
        e.insert(0, g_fnum / second)    

def button_sub():
    first = e.get()
    global g_fnum 
    global math
    math = "-"
    g_fnum = int(first) 
    e.delete(0, END)

def button_mult():
    first = e.get()
    global g_fnum 
    global math
    math = "*"
    g_fnum = int(first) 
    e.delete(0, END)
        
def button_divide():
    first = e.get()
    global g_fnum 
    global math
    math = "/"
    g_fnum = int(first) 
    e.delete(0, END)


b1 = Button(w,text="1", padx=40, pady=20, command=lambda: button_click(1))
b2 = Button(w,text="2", padx=40, pady=20, command=lambda: button_click(2))
b3 = Button(w,text="3", padx=40, pady=20, command=lambda: button_click(3))
b4 = Button(w,text="4", padx=40, pady=20, command=lambda: button_click(4))
b5 = Button(w,text="5", padx=40, pady=20, command=lambda: button_click(5))
b6 = Button(w,text="6", padx=40, pady=20, command=lambda: button_click(6))
b7 = Button(w,text="7", padx=40, pady=20, command=lambda: button_click(7))
b8 = Button(w,text="8", padx=40, pady=20, command=lambda: button_click(8))

b9 = Button(w,text="9", padx=40, pady=20, command=lambda: button_click(9))
b0 = Button(w,text="0", padx=40, pady=20, command=lambda: button_click(0))
bA = Button(w,text="+", padx=38, pady=20, command=button_add)
bE = Button(w,text="=", padx=87, pady=20, command=button_equal)
bC = Button(w,text="C", padx=89, pady=20, command=button_clear)

bS = Button(w,text="-", padx=41, pady=20, command=button_sub)
bM = Button(w,text="x", padx=40, pady=20, command=button_mult)
bD = Button(w,text="/", padx=41, pady=20, command=button_divide)


# place buttons on screen top->down
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b0.grid(row=4, column=0)
bA.grid(row=5, column=0)
bC.grid(row=4, column=1, columnspan=2)
bE.grid(row=5, column=1, columnspan=2)

bS.grid(row=6, column=0)
bM.grid(row=6, column=1)
bD.grid(row=6, column=2)
w.mainloop()