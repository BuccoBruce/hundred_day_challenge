from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
def known_card():
    global to_learn, current_card, new_data

    for d in to_learn:
        if d["French"] == current_card["French"]:
            to_learn.remove(d)
            print(f"Removing {d["French"]} from csv.")
    new_data = pd.DataFrame(to_learn)
    new_file = new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global current_card, delay, to_learn, new_data

    window.after_cancel(delay)
    if os.path.isfile("data/words_to_learn.csv"):
        data = pd.read_csv("data/words_to_learn.csv")
        to_learn = data.to_dict(orient="records")
    next_card = random.choice(to_learn)
    current_card = next_card
    current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=next_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    delay = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

delay = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# Flash Card
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, border=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, border=0, command=known_card)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
