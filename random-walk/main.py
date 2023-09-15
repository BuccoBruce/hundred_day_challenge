from turtle import Turtle, Screen
import random


def random_color():
    t.color(random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))
    return


def random_direction():
    headings = [0, 90, 180, 270]
    heading = random.choice(headings)
    t.setheading(heading)
    return


# Set turtle and screen attributes
t = Turtle()
t.speed(0)
s = Screen()
s.colormode(255)
t.shape("turtle")
t.pensize(10)

# Set initial random values
random_direction()
random_color()

# Move forward or backward
# Buffer old direction for comparison
# If direction is changing, then also change color of line
for _ in range(500):
    paces = random.choice([20, -20])
    t.forward(paces)
    old_direction = t.heading()
    random_direction()
    new_direction = t.heading()
    # Change color if direction of movement has changed
    if not new_direction == old_direction:
        random_color()
s.exitonclick()
