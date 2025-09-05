from tkinter import *

from PIL import ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

timer_label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), fg=GREEN,bg=YELLOW)
timer_label.grid(column=1, row=0)

def checkbutton_used():
    pass
start = Button(text="Start",command=checkbutton_used, highlightthickness=0, bg="white")
start.grid(column=0, row=2)

reset = Button(text="Reset", command=checkbutton_used, highlightthickness=0, bg="white")
reset.grid(column=2, row=2)

text = "✔"
check_label = Label(text=text, font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
PhotoImage = ImageTk.PhotoImage(file="tomato.png")
canvas.create_image(101,112,image=PhotoImage)
canvas.create_text(101,133,text="00:00",font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()