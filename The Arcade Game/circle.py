from turtle import Turtle


class Circle (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=3, stretch_wid=3)
        self.color("grey")
        self.penup()
        self.goto(0, 0)