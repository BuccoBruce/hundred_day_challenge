from turtle import Turtle

UP = 90
DOWN = 270


class PlayerPaddle(Turtle):
    def __init__(self):
        self.x = -400
        self.y = 20
        self.paddle_list = []
        self.create_paddle()
        self.head = self.paddle_list[0]
        for segment in self.paddle_list:
            segment.setheading(UP)

    def create_paddle(self):
        for _ in range(3):
            paddle = Turtle(shape="square")
            paddle.color("white")
            paddle.penup()
            paddle.setx(self.x)
            paddle.sety(self.y)
            self.y -= 20
            self.paddle_list.append(paddle)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)

    def move(self):
        for seg_num in range(len(self.paddle_list) - 1, 0, -1):
            new_x = self.paddle_list[seg_num - 1].xcor()
            new_y = self.paddle_list[seg_num - 1].ycor()
            self.paddle_list[seg_num].goto(new_x, new_y)
        self.head.forward(20)

class CPUPaddle():
    def __init__(self):
        self.x = 400
        self.y = 20
        self.paddle_list = []
        self.create_paddle()
        self.head = self.paddle_list[0]
        self.pos = self.paddle_list[1].ycor()

    def create_paddle(self):
        for _ in range(3):
            paddle = Turtle(shape="square")
            paddle.color("white")
            paddle.penup()
            paddle.setx(self.x)
            paddle.sety(self.y)
            self.y -= 20
            self.paddle_list.append(paddle)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)

    def move(self):
        for seg_num in range(len(self.paddle_list) - 1, 0, -1):
            new_x = self.paddle_list[seg_num - 1].xcor()
            new_y = self.paddle_list[seg_num - 1].ycor()
            self.paddle_list[seg_num].goto(new_x, new_y)
        self.head.forward(10)
