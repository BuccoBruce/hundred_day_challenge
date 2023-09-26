from turtle import Turtle

COLOR = "white"
SPEED = "fastest"
ALIGNMENT = "center"
FONT_FACE = "Courier"
FONT_SIZE = 16
FONT_TYPE = "bold"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.cpu_score = 0
        self.color(COLOR)
        self.penup()
        self.speed(SPEED)
        self.goto(x=0, y=280)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(
            f"{self.player_score} | {self.cpu_score}",
            False,
            align=ALIGNMENT,
            font=(FONT_FACE, FONT_SIZE, FONT_TYPE))

    def increase_score(self, player):
        if player == "player":
            self.player_score += 1
        elif player == "cpu":
            self.cpu_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT_FACE, FONT_SIZE, FONT_TYPE))

    def you_win(self):
        self.goto(0, 0)
        self.clear()
        self.color("green")
        self.write(f"YOU WON!!!", align=ALIGNMENT, font=(FONT_FACE, 24, FONT_TYPE))