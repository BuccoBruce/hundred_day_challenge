import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Quiz")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_list = data["state"].tolist()
answer_list = []
states_to_learn = []

score = 0
game_is_on = True

while game_is_on:

    screen_title = f"Guess the State {score}/50"
    answer_state = screen.textinput(title=screen_title, prompt="What's another state?").title()
    if answer_state in data.values and answer_state not in answer_list:
        x_val = data.loc[data["state"] == answer_state, "x"]
        x_val = x_val.to_list()[0]

        y_val = data.loc[data["state"] == answer_state, "y"]
        y_val = y_val.to_list()[0]

        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x_val, y_val)
        state.write(f"{answer_state}")

        answer_list.append(answer_state)
        score += 1
    elif answer_state in answer_list:
        print(f"You already guessed {answer_state}!")
    elif score >= 50:
        print("You win!")
        game_is_on = False
    elif answer_state == "Exit":
        break
    else:
        print(f"{answer_state} is not a state.")

# states to learn.csv
for state in state_list:
    if state not in answer_list:
        states_to_learn.append(state)

states_to_learn_dict = {
    "state": states_to_learn
}

df = pd.DataFrame(states_to_learn_dict)
df.to_csv("states_to_learn.csv")
