from turtle import Turtle, Screen
import random

is_race_on = False
s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-150, -100, -50, 0, 50, 100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[turtle_index])
    all_turtles.append(new_turtle)

print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The winning color is {winning_color}")
            else:
                print(f"You lost, the winner is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

s.exitonclick()