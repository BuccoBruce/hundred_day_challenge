from turtle import Turtle
import random

STARTING_DIR = [35, 125, 215, 305]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.ball = Turtle(shape="square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.setx(self.x)
        self.ball.sety(self.y)
        self.ball.setheading(random.choice(STARTING_DIR))

    def move(self):
        self.ball.forward(20)

    def bounce(self):
        self.ball.setheading(self.ball.heading() + 180)

    def deflect(self):
        self.ball.setheading((self.ball.heading() * -1) % 360)

    def reset_ball(self):
        self.ball.setx(0)
        self.ball.sety(0)
        self.ball.setheading(random.choice(STARTING_DIR))
