import email
from tkinter import *
from PIL import ImageTk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(window, width=200, height=200)
logo = ImageTk.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email.label = Label(text="Email/Username")
email.label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=39)
website_entry.grid(row=1, column=1,columnspan=2)
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1,columnspan=2)
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password",width=13)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add",width=39)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()