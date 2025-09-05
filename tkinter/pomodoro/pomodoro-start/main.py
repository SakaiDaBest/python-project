from tkinter import *
import time
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
def start_timer():
    countdown(25,00)

def reset_timer():
    canvas.itemconfig(timer_text, text=f"00:00")
    check_label.config(text="")
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

text = ''
check_label = Label(text=text, font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)


canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
PhotoImage = ImageTk.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=PhotoImage)
timer_text = canvas.create_text(103,133,text="00:00",font=(FONT_NAME, 32, "bold"),fill="white")
canvas.grid(column=1, row=1)

def countdown(min, sec):
    current_text = check_label.cget("text")
    # Format time nicely as MM:SS
    canvas.itemconfig(timer_text, text=f"{min}:{sec:02}")

    if sec <= 0 and min != 0:  # logical AND, not bitwise
        window.after(1000, lambda: countdown(min-1, 59))
    elif sec >= 0:
        if not (min == 0 and sec == 0):
            window.after(1000, lambda: countdown(min, sec-1))

    elif sec ==0 and min ==0 and current_text != "✔✔✔✔":
        # get current text from label
        check_label.config(text=current_text + "✔")
        breaktimer(5, 0)
    elif current_text == "✔✔✔✔":
        breaktimer(15, 0)

def breaktimer(min, sec):
    canvas.itemconfig(timer_text, text=f"{min}:{sec:02}")

    if sec <= 0 and min != 0:  # logical AND, not bitwise
        window.after(1000, lambda: breaktimer(min - 1, 59))
    elif sec >= 0:
        if not (min == 0 and sec == 0):
            window.after(1000, lambda: breaktimer(min, sec - 1))
    elif sec ==0 and min ==0:
        # get current text from label
        countdown(25, 0)


start = Button(text="Start",command=start_timer(), highlightthickness=0, bg="white")
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer(), highlightthickness=0, bg="white")
reset.grid(column=2, row=2)


window.mainloop()