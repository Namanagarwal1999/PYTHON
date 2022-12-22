from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middle import Middle
from circle import Circle
import time

screen = Screen()
screen.setup(800, 600)
SLEEP_TIME = 0.1

screen.bgcolor("black")
screen.title("Arcade Game")
screen.tracer(0)

l_paddle = Paddle((-360, 0))
r_paddle = Paddle((360, 0))
scoreboard = Scoreboard()
middle = Middle()
circle = Circle()

ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on and (scoreboard.l_score <= 5 and scoreboard.r_score <= 5):
    time.sleep(SLEEP_TIME)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_wall()

    if r_paddle.distance(ball) < 30 or l_paddle.distance(ball) < 30 or r_paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        SLEEP_TIME *= 0.9
        print (SLEEP_TIME)


    if ball.xcor() > 410:
        scoreboard.increase_score_l()
        ball.new_ball()
        SLEEP_TIME = 0.1


    if ball.xcor() < -410:
        scoreboard.increase_score_r()
        ball.new_ball()
        SLEEP_TIME = 0.1

else:
    if scoreboard.l_score > 5:
        scoreboard.player1_win()

    else:
        scoreboard.player2_win()


screen.exitonclick()