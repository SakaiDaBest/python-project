import tkinter

window = tkinter.Tk()
window.title("My first")
window.minsize(width=100,height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic", "bold"))
my_label.pack(side="left", expand=True)


window.mainloop()