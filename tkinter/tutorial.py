from tkinter import *

window = Tk()
window.title("My first")
window.minsize(width=100,height=300)

my_label = Label(text="I am a label", font=("Arial", 24, "italic", "bold"))
my_label.pack(side="left", expand=True)

my_label["text"] = "I am a label"
my_label.config(text="I am a label")

def button_clicked():
    new_text = input.get()
    print("I got clicked")
    my_label.config(text=new_text)

button = Button(window, text="Click me", command = button_clicked)
button.pack(side="right")

input = Entry()
input.pack(side="left")


window.mainloop()