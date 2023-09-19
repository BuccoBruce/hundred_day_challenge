from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for position in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.setx(self.x)
            snake.sety(self.y)
            self.x -= 20
            self.snake_list.append(snake)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.setx(self.snake_list[-1].xcor())
        snake.sety(self.snake_list[-1].ycor())
        if self.head.heading == UP:
            self.y -= 20
        elif self.head.heading == DOWN:
            self.y += 20
        elif self.head.heading == RIGHT:
            self.x -= 20
        elif self.head.heading == LEFT:
            self.x += 20
        self.snake_list.append(snake)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())
