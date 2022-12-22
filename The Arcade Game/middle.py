from turtle import Turtle


class Middle (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.10, stretch_wid=28)
        self.color("grey")
        self.penup()
        self.goto(0, 0)