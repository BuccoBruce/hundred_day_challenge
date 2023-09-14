from turtle import Turtle, Screen
import random


def random_color():
    t.color(random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))
    return


# Set turtle and screen attributes
t = Turtle()
t.speed(0)
s = Screen()
s.colormode(255)
t.pensize(1)
random_color()

for _ in range(72):
    t.circle(100.0)
    t.setheading(t.heading() + 5.0)
    random_color()
s.exitonclick()
