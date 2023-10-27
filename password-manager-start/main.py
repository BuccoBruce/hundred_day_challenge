from tkinter import *

WHITE = "#ffffff"
EMAIL_ADDRESS = "dcmcmillan@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")

# Image
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entry Fields
website_entry = Entry(width=35)
email_username_entry = Entry(width=35)
password_entry = Entry(width=21)

website_entry.focus()
email_username_entry.insert(0, EMAIL_ADDRESS)

website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
gen_pass_button = Button(text="Generate Password")
add_button = Button(text="Add", width=36)

gen_pass_button.grid(column=2, row=3, sticky="EW")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")



window.mainloop()