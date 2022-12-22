from turtle import Turtle

class Ball(Turtle):
    # RANDOM = random.randint(0, 360)

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.increased_speed = 0
        self.x_move = 10
        self.y_move = 10

    def new_ball(self):
        self.goto(0, 0)
        self.bounce_paddle()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1





