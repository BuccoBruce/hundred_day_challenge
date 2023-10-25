from tkinter import *

WHITE = "#ffffff"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)


window.mainloop()
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #