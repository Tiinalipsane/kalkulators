from tkinter import *
import tkinter as tk
from tkinter import ttk
from math import *

Kalk=tk.Tk()
Kalk.title("Kalkulators")
Kalk.geometry("567x684")


def btnClick(number):
    current=e.get() #nolasa esošo skaitli
    e.delete(0,END) #nodzēš
    nexNumber=str(current)+str(number)
    e.insert(0,nexNumber) # ievieto displejā
    return 0

def vienads():
    global num2
    num2=(float(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="÷":
        result=num1/num2
    elif mathOp=="÷":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def btnCommand(command):
    global number
    global mathOp
    global num1
    global num3
    mathOp=command #+*/-
    num1=(float(e.get()))
    e.delete(0,END)
    return 0

def Clear():
    e.delete(0,END)
    num1 = 0
    mathOp=""
    return 0

    

e=Entry(Kalk, width=15, bd=20, font=("Arial Black",20), bg="pink")
e.grid(row=0, column=0, columnspan=4)


btnC=Button(Kalk, text="C",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink",command=Clear)
btnC.grid(row=1, column=0)
btnC.config(width=2, height=1)

btnkvadr=Button(Kalk, text="x2",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink")
btnkvadr.grid(row=1, column=1)
btnkvadr.config(width=2, height=1)

btnsakne=Button(Kalk, text="√x",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink")
btnsakne.grid(row=1, column=2)
btnsakne.config(width=2, height=1)

btndalit=Button(Kalk, text="÷",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink", command=lambda:btnCommand("÷"))
btndalit.grid(row=1, column=3)

btn7=Button(Kalk, text="7",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(7))
btn7.grid(row=2, column=0)
btn7.config(width=2, height=1)

btn8=Button(Kalk, text="8",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(8))
btn8.grid(row=2, column=1)
btn8.config(width=2, height=1)

btn9=Button(Kalk, text="9",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(9))
btn9.grid(row=2, column=2)
btn9.config(width=2, height=1)

btnreiz=Button(Kalk, text="*",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink", command=lambda:btnCommand("*"))
btnreiz.grid(row=2, column=3)
btnreiz.config(width=2, height=1)

btn4=Button(Kalk, text="4",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(4))
btn4.grid(row=3, column=0)
btn4.config(width=2, height=1)

btn5=Button(Kalk, text="5",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(5))
btn5.grid(row=3, column=1)
btn5.config(width=2, height=1)

btn6=Button(Kalk, text="6",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(6))
btn6.grid(row=3, column=2)
btn6.config(width=2, height=1)

btnminus=Button(Kalk, text="-",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink", command=lambda:btnCommand("-"))
btnminus.grid(row=3, column=3)
btnminus.config(width=2, height=1)

btn1=Button(Kalk, text="1",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(1))
btn1.grid(row=4, column=0)
btn1.config(width=2, height=1)

btn2=Button(Kalk, text="2",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(2))
btn2.grid(row=4, column=1)
btn2.config(width=2, height=1)

btn3=Button(Kalk, text="3",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(3))
btn3.grid(row=4, column=2)
btn3.config(width=2, height=1)

btnplus=Button(Kalk, text="+",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink", command=lambda:btnCommand("+"))
btnplus.grid(row=4, column=3)
btnplus.config(width=2, height=1)

btnpm=Button(Kalk, text="+/-",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink")
btnpm.grid(row=5, column=0)
btnpm.config(width=2, height=1)

btn0=Button(Kalk, text="0",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="pink", command=lambda:btnClick(0))
btn0.grid(row=5, column=1)
btn0.config(width=2, height=1)

btnlog=Button(Kalk, text="log",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink")
btnlog.grid(row=5, column=2)
btnlog.config(width=2, height=1)

btnir=Button(Kalk, text="=",padx="40", pady="20", bd=10,font=("Arial Black",20), bg="hot pink", command=vienads)
btnir.grid(row=5, column=3)
btnir.config(width=2, height=1)







Kalk.mainloop()