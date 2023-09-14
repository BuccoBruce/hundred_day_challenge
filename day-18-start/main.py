from turtle import Turtle, Screen
import random
my_turtle = Turtle()

my_screen = Screen()
my_screen.colormode(255)
turns = 3
for _ in range(8):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # my_turtle.pencolor(red, green, blue)
    my_turtle.color(red, green, blue)
    for _ in range(turns):
        my_turtle.forward(50)
        my_turtle.right(360/turns)
    turns += 1

my_screen.exitonclick()
