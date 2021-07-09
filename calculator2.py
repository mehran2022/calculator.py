#we want create gui calculator
#we only first imported tk inteter until graphik  
import time
from tkinter import *

expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression =""
	except:
		equation.set(" error.please write a number")
		expression = ""
def clear():
	global expression
	expression = ""
	equation.set("")
if __name__ == "__main__":
    win = Tk()
    win.title("calculator")
    win.configure(bg="black")
    equation = StringVar()
    expression_field = Entry(win,textvariable=equation,width=30,fg="green",bg="black",cursor="mouse",font=("arial",30))
    expression_field.grid(row=10,column=10)
    b7 = Button(win,text="0",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(0))
    b7.grid(row = 10,column = 3)
    n1 = Button(win,text="1",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(1))
    n1.grid(row=1,column=2)
    n2 = Button(win,text="2",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(2))
    n2.grid(row=2,column=2)
    n3 = Button(win,text="3",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(3))
    n3.grid(row=9,column=2)
    n4 = Button(win,text="4",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(4))
    n4.grid(row=1,column=3)
    n5 = Button(win,text="5",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(5))
    n5.grid(row=2,column=3)
    n6 = Button(win,text="6",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(6))
    n6.grid(row=9,column=3)
    n7 = Button(win,text="7",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(7))
    n7.grid(row=1,column=4)
    n8 = Button(win,text="8",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(8))
    n8.grid(row=2,column=4)
    n9 = Button(win,text="9",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press(9))
    n9.grid(row=9,column=4) 
    n10 = Button(win,text="=",font=50,bd=10,fg = "red",cursor="hand2",command=equalpress)
    n10.grid(row=9,column=5)
    b = Button(win,text="*",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press("*"))
    b.grid(row=1,column=1)
    b2 = Button(win,text="/",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press("/"))
    b2.grid(row=2,column=1)
    b3 = Button(win,text=".",font=100,bd = 5,fg = "black",cursor="hand2",command=lambda: press("."))
    b3.grid(row=9,column=1)
    b4 = Button(win,text="-",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press("-"))
    b4.grid(row=10,column=1)
    b5 = Button(win,text="+",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press("+"))
    b5.grid(row=10,column=4)
    b6 = Button(win,text="%",font=30,bd = 5,fg = "black",cursor="hand2",command=lambda: press("%"))
    b6.grid(row = 10,column=2)
    c = Button(win,text="CLEAR",font=60,bd = 5,fg = "black",cursor="hand2",command=clear)
    c.grid(row=10,column=5)
t=""
c2 = Label(win,font = ("times",40,"bold"),bg = "black",fg="yellow",cursor="star")
c2.grid(row=1,column=10)
c3 = Label(win,text="(time to TEHRAN)",font=("arial",30),bg="black",fg="yellow")
c3.grid(row=2,column=10)
w=Label(win,text="WELLCOME TO calculator",font=("arial",30),fg="red",bg="black")
w.grid(row=1,column=8)
def tick():
    global t
    time2 = time.strftime("%H : %M : %S")
    if time2 != t:
        t = time2
        c2.config(text = time2)
    c2.after(200,tick)
tick()
win.mainloop()




