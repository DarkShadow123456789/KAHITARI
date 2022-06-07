from datetime import datetime, date
from tkinter import *
from MySQLdb import Date
from PIL import Image, ImageTk
import mysql.connector
import tkinter.messagebox as m


w = Tk()
w.geometry("500x900")
w.state("zoomed")
w.title("Flour Application")


def Insertdata():
    i = id.get()
    n = name.get()
    a = avalue.get()
    d = datetime.now().date()

    if(i == '' or n == '' or a == '' or d == ''):
        m.showinfo("insert status", "all fields are mandatory")
    else:
        try:
            conn = mysql.connector.connect(host='localhost',user='root',password='root',database='flour')
            cursor = conn.cursor()
            args = (i, n, a, d)
            query = "insert into customer values(%s,%s,%s,%s)"
            cursor.execute(query, args)
            conn.commit()
            m.showinfo("data inserted successfully")
            conn.close()
        except Exception as ee:
            print("insert exception", ee)

    
def Deletedata():
    idinput= id.get()
    # n = name.get()
    # a = avalue.get()
    # d = datetime.now().date()

    

    if(idinput == ''):
       m.showinfo("insert status", "Id field is mandatory")
    else:
        try:
            conn = mysql.connector.connect(host='localhost',user='root',password="root",database='flour')
            cursor = conn.cursor()
            args = idinput
            query = "delete from customer where id=%d"
            cursor.execute(query,args)
            conn.commit()
            m.showinfo("data deleted successfully")
            conn.close()
        except Exception as ee:
            print("insert exception", ee)        


# Declaration

id = IntVar()
fvalue = IntVar()
avalue = IntVar()
name = StringVar()


f1 = Frame(w, borderwidth=10, relief=SUNKEN, bg="gray")
f1.pack(side=LEFT, fill=Y)

f2 = Frame(w, borderwidth=6, relief=SUNKEN, bg="tomato")
f2.pack(side=TOP, fill=X)


image = Image.open("flour.jpeg")
photo = ImageTk.PhotoImage(image)


def wheat(event):
    avalue.set(fvalue.get()*5)


def millet(event):
    avalue.set(fvalue.get()*7)


def pulse(event):
    avalue.set(fvalue.get()*2)



l1 = Label(f1, image=photo)
l1.pack(pady=170)

l2 = Label(f2, text="Flour Application", fg="black", font="serif 20 bold")
l2.pack()


lid = Label(w, text="ID", font="serif 20 bold")
lid.place(x=950, y=90)


eid = Entry(font="lucida 20 bold", textvariable=id)
eid.place(x=1050, y=90)


l3 = Label(w, text="Name ", font="lucida 20 bold")
l3.place(x=900, y=150)

e1 = Entry(font="lucida 20 bold", textvariable=name)
e1.place(x=1050, y=150,)

l4 = Label(w, text="Flour (Kg)", font="lucida 20 bold")
l4.place(x=900, y=250)


e2 = Entry(font="lucida 15 bold", textvariable=fvalue, justify=CENTER)
e2.place(x=1050, y=250,)

b1 = Button(w, text="Wheat", font="lucida 20 bold", bg="tan")
b1.place(x=990, y=350)
b1.bind("<Button-1>", wheat)

b2 = Button(w, text="Millet", font="lucida 20 bold", bg="tan")
b2.place(x=1150, y=350)
b2.bind("<Button-1>", millet)

b3 = Button(w, text="Pulse", font="lucida 20 bold", bg="tan")
b3.place(x=1300, y=350)
b3.bind("<Button-1>", pulse)

l3 = Label(w, text="Amount", font="lucida 20 bold")
l3.place(x=900, y=500)


e3 = Entry(w, font="lucida 15 bold", textvariable=avalue, justify=CENTER)
e3.place(x=1050, y=500)

l4 = Label(w, text=" Flour Mill", font="lucida 30 bold",
           fg="white", bg="gray", borderwidth=15)
l4.place(x=190, y=60)
date = datetime.now().date()
l4 = Label(w, text=date, font="vardana 15 bold", fg="black")
l4.place(x=1400, y=60)

b4 = Button(w, text="Insert", font="lucida 20 bold", bg="lime",command=lambda:Insertdata())
b4.place(x=850, y=600)

b5 = Button(w, text="Delete", font="lucida 20 bold",bg="red",command=lambda:Deletedata())
b5.place(x=1020, y=600)
b6 = Button(w, text="Update", font="lucida 20 bold",bg="skyblue")
b6.place(x=1200, y=600)
b7 = Button(w, text="Clear", font="lucida 20 bold", bg="yellow")
b7.place(x=1400, y=600)


b8 = Button(w, text="Print", font="lucida 20 bold",bg="pink")
b8.place(x=1120, y=720)


w.mainloop()
