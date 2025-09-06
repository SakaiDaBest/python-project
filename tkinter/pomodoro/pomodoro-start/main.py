from tkinter import *
from PIL import ImageTk


GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

timer_on = False

def start_timer():
    global timer_on
    if not timer_on:
        timer_on = True
        countdown(25, 0)

def reset_timer():
    global timer_on
    timer_on = False
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)


timer_label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), fg=GREEN,bg=YELLOW)
timer_label.grid(column=1, row=0)


text = ''
check_label = Label(text=text, font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)


canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
PhotoImage = ImageTk.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=PhotoImage)
timer_text = canvas.create_text(103,133,text="00:00",font=(FONT_NAME, 32, "bold"),fill="white")
canvas.grid(column=1, row=1)

def countdown(min, sec):
    global timer_on
    if timer_on:
        current_text = check_label.cget("text")
        canvas.itemconfig(timer_text, text=f"{min:02}:{sec:02}")

        if sec <= 0 and min != 0:
            window.after(1000, lambda: countdown(min - 1, 59))
        elif sec > 0:
            window.after(1000, lambda: countdown(min, sec - 1))
        elif min == 0 and sec == 0:
            if current_text != "✔✔✔✔":
                check_label.config(text=current_text + "✔")
                breaktimer(5, 0)
            else:
                breaktimer(15, 0)
def breaktimer(min, sec):
    global timer_on
    current_text = check_label.cget("text")
    if timer_on:
        canvas.itemconfig(timer_text, text=f"{min:02}:{sec:02}")

        if sec <= 0 and min != 0:
            window.after(1000, lambda: breaktimer(min - 1, 59))
        elif sec > 0:
            window.after(1000, lambda: breaktimer(min, sec - 1))
        elif min == 0 and sec == 0 and current_text != "✔✔✔✔":
            countdown(25, 0)



start = Button(text="Start",command=start_timer, highlightthickness=0, bg="white")
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer, highlightthickness=0, bg="white")
reset.grid(column=2, row=2)


window.mainloop()