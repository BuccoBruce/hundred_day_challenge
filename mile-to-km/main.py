from tkinter import *


def button_clicked():
    new_data = round(float(entry.get()) * 1.609)
    label_km_data.config(text=new_data)


window = Tk()
window.title("Mike to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=20)

# Labels
label_miles = Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=2, row=0)

label_is_equal_to = Label(text="is equal to", font=("Arial", 12))
label_is_equal_to.grid(column=0, row=1)

label_km_data = Label(text="0", font=("Arial", 12))
label_km_data.grid(column=1, row=1)

label_km = Label(text="Km", font=("Arial", 12))
label_km.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

window.mainloop()

