from tkinter import *

window = Tk()
window.title("Unit Converter")
window.resizable(width=0, height=0)

conv = [1.61, 1/12, 1/2.54, 1/30.48]

con_type1 = Label(window, text="Mile")
con_type2 = Label(window, text="Kilometer")
con_type1.grid(column=0, row=1)
con_type2.grid(column=0, row=3)

def update_first(*args):
    if input1.get() == "":
        input2.set("")
        return
    try:
        num = conv[unitOption.get()]
        input2.trace_remove("write", trace2)
        input2.set(float(input1.get()) / num)
        input2.trace_add("write", update_second)
    except ValueError:
        input2.set("")

def update_second(*args):
    if input2.get() == "":
        input1.set("")
        return
    try:
        num = conv[unitOption.get()]
        input1.trace_remove("write", trace1)
        input1.set(float(input2.get()) * num)
        input1.trace_add("write", update_first)
    except ValueError:
        input1.set("")

def conversion():
    choice = unitOption.get()
    input2.set("")
    input1.set("")

    if choice == 0:
        con_type1.configure(text="Mile")
        con_type2.configure(text="Kilometer")
    elif choice == 1:
        con_type1.configure(text="Feet")
        con_type2.configure(text="Inch")
    elif choice == 2:
        con_type1.configure(text="Inch")
        con_type2.configure(text="Centimetre")
    elif choice == 3:
        con_type1.configure(text="Feet")
        con_type2.configure(text="Centimetres")

title = Label(text="UNIT CONVERTER", font=("Arial", 24, "bold"))
title.grid(column=0, row=0)

unitOption = IntVar()
Radiobutton(window, text="mile to km", variable=unitOption, value=0, command=conversion).grid(row=1, column=1)
Radiobutton(window, text="feet to inch", variable=unitOption, value=1, command=conversion).grid(row=2, column=1)
Radiobutton(window, text="inch to cm", variable=unitOption, value=2, command=conversion).grid(row=3, column=1)
Radiobutton(window, text="feet to cm", variable=unitOption, value=3, command=conversion).grid(row=4, column=1)

input1 = StringVar()
input2 = StringVar()

entry1 = Entry(window, textvariable=input1)
entry1.grid(row=2, column=0)
entry2 = Entry(window, textvariable=input2)
entry2.grid(row=4, column=0)

trace1 = input1.trace_add("write", update_first)
trace2 = input2.trace_add("write", update_second)

window.mainloop()
