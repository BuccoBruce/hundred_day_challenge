from turtle import Turtle, Screen
import random


def random_color():
    color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5),
                  (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12),
                  (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11),
                  (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168),
                  (93, 233, 198), (65, 231, 239), (217, 88, 51)]
    new_color = (random.choice(color_list))
    return new_color


def draw_filled_circles():
    t.begin_fill()
    t.pendown()
    t.circle(RADIUS)
    t.end_fill()
    t.penup()
    t.forward(DISTANCE)
    module_color = random_color()
    t.color(module_color)
    t.fillcolor(module_color)


RADIUS = 10
DISTANCE = 50
STEPS = 10

x = -400
y = -300
color = random_color()

# Initialize Screen attributes
s = Screen()
s.colormode(255)

# Initialize turtle color and position
t = Turtle()
t.color(color)
t.fillcolor(color)
t.hideturtle()
t.penup()
t.setx(x)
t.sety(y)
t.speed("fastest")

# Iterate over STEPS, drawing filled circles.  When a row is completed,
# reset turtle X to start position, increase Y by distance between circles.
for _ in range(STEPS):
    y += DISTANCE
    t.sety(y)
    t.setx(x)
    for _ in range(STEPS):
        draw_filled_circles()

s.exitonclick()
