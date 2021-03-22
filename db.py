from tkinter import *
import sqlite3

w = Tk()
w.title("database")
w.geometry("400x400")


# create table
# c.execute("""
#     CREATE TABLE stuff ( 
#     name text, age integer 
#     )""")

name = Entry(w, width=20)
name.grid(row=0, column=1, padx=20)
age = Entry(w, width=20)
age.grid(row=1, column=1, padx=20)
record = Entry(w,width=5)
record.grid(row=4, column=0)


def delete():
    # create a connection to db
    conn = sqlite3.connect('stuff.db')

    # create a cursor
    c = conn.cursor()

    c.execute("DELETE FROM stuff WHERE oid= " + record.get())


    # save changes
    conn.commit()

    # close connection
    conn.close()



def show():
    # create a connection to db
    conn = sqlite3.connect('stuff.db')

    # create a cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM stuff")    # oid is a sqlite UID
    r = c.fetchall()
    print(r)

    allrecs = ''
    for rec in r:
        allrecs += str(rec[0]) + "\t" + str(rec[1]) + "\t" + str(rec[2]) + "\n"

    outputlbl = Label(w, text=allrecs).grid(row=5, column=0, columnspan=2)
    
    # save changes
    conn.commit()

    # close connection
    conn.close()





def submit():
    # create a connection to db
    conn = sqlite3.connect('stuff.db')

    # create a cursor
    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO stuff VALUES (:name, :age)",
        {
            'name': name.get(),
            'age': age.get()
        })

    # clear text boxes
    name.delete(0,"end")
    age.delete(0,"end")

    # save changes
    conn.commit()

    # close connection
    conn.close()



namelab = Label(w, text="Name: ").grid(row=0, column=0)
agelab = Label(w, text="Age: ").grid(row=1, column=0)

submitbtn = Button(w, text="Submit", command=submit).grid(row=2, column=1)
showbtn = Button(w, text="Show", command=show).grid(row=3, column=1)
delbtn = Button(w, text="Delete", command=delete).grid(row=4, column=1)


w.mainloop()