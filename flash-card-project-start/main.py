from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# Flash Card
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")

unknown_button = Button(image=cross_image, highlightthickness=0, border=0)
known_button = Button(image=check_image, highlightthickness=0, border=0)

unknown_button.grid(column=0, row=1)
known_button.grid(column=1, row=1)

window.mainloop()
