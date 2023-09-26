from paddle import PlayerPaddle, CPUPaddle
from ball import Ball
from scoreboard import ScoreBoard
from turtle import Screen
import time

screen = Screen()
screen.title("PONG")
screen.setup(1000, 1000)
screen.tracer(0)
screen.bgcolor("black")

player_paddle = PlayerPaddle()
cpu_paddle = CPUPaddle()
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(player_paddle.up, "Up")
screen.onkey(player_paddle.down, "Down")

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    player_paddle.move()
    ball.move()

    # CPU Movement AI
    if cpu_paddle.head.ycor() > ball.ball.ycor():
        cpu_paddle.down()
        cpu_paddle.move()
    elif cpu_paddle.head.ycor() < ball.ball.ycor():
        cpu_paddle.up()
        cpu_paddle.move()

    # Player Paddle Collision Detection
    for segment in player_paddle.paddle_list:werv
        if segment.distance(ball.ball) < 50:
            ball.bounce()

    # CPU Paddle Collision Detection
    for segment in cpu_paddle.paddle_list:
        if segment.distance(ball.ball) < 50:
            ball.bounce()

    # Ball bounce on walls
    if ball.ball.ycor() > 400 or ball.ball.ycor() < -400:
        print("Bounce for y!")
        ball.deflect()

    # Score detection
    if ball.ball.xcor() > 400:
        scoreboard.increase_score("player")
        ball.reset_ball()
    elif ball.ball.xcor() < -400:
        scoreboard.increase_score("cpu")
        ball.reset_ball()

    # Control speed of game
    time.sleep(1/10)

screen.exitonclick()
