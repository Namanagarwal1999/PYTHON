from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(700, 700)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "8")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # screen.update()
    time.sleep(0.1)
    screen.update()

    snake.move()

    #Detect collusion with food
    score_count = 0
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collusion with wall
    if snake.head.xcor() > 345 or snake.head.xcor() < -345 or snake.head.ycor() > 345 or snake.head.ycor() < -345:
        scoreboard.reset()
        snake.reset()

    # Detect collusion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

















screen.exitonclick()
