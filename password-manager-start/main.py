from tkinter import *
from tkinter import messagebox

WHITE = "#ffffff"
EMAIL_ADDRESS = "dcmcmillan@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.csv", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    

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
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entry Fields
website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)

website_entry.focus()
email_entry.insert(0, EMAIL_ADDRESS)

website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
gen_pass_button = Button(text="Generate Password")
add_button = Button(text="Add", width=36, command=save_data)

gen_pass_button.grid(column=2, row=3, sticky="EW")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
