from tkinter import *
p = "please write here"
c = "please write your phone number here"
win = Tk()
win.title("SIGN IN")
win.resizable(False,False)
win.config(bg="purple")
list1 = Listbox(win,bg="blue",fg="black",height=10,width=30,font=("arial",30))
list1.grid(row=16,column=1)
def d():
    fname.delete(0,"end")
def l_reset():
    list1.delete(0,"end")
def delete():
   namee.delete(0, 'end')
def delete2():
    pphone.delete(0,"end")
def press():
    global press
fname = Entry(win,bg="black",fg="white",font=("arial",20))
fname.grid(row=1,column=1)
label3 = Label(win,text="please write your family name here:",bg="black",fg="red",font=("arial",20))
label3.grid(row=1,column=0)
namee = Entry(win,bg="black",fg="white",font=("arial",20))
namee.grid(row=2,column=1)
label = Label(win,text="please write your name here:",bg="black",fg="red",font=("arial",20))
label.grid(row=2,column=0)
pphone = Entry(win,bg="black",fg="white",font=("arial",20))
pphone.grid(row=3,column=1)
label2 = Label(win,text="please write your phone here:",bg="black",fg="red",font=("arial",20))
label2.grid(row=3,column=0)
addd = Button(win,text="add",bg="yellow",fg="red",font=("arial",20),command=lambda:(list1.insert(1,namee.get(),fname.get(),"ADDED")))
addd.grid(row=1,column=12)
DELETEe = Button(win,text="DELET",bg="yellow",fg="red",font=("arial",20),command=lambda:(delete(),delete2(),d()))
DELETEe.grid(row=1,column=10)
resett = Button(win,text="reset",bg="yellow",fg="red",font=("arial",20),command=lambda:(l_reset()))
resett.grid(row=3,column=12)
exitt = Button(win,text="QUITE",bg="yellow",fg="red",font=("arial",20),command=(quit))
exitt.grid(row=3,column=10)
enter = Button(win,text="ENTER",bg="yellow",fg="red",font=("arial",20),command=lambda:(list1.insert(1,namee.get(),fname.get(),"ADDED")))
enter.grid(row=4,column=1)
win.mainloop()