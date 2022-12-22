from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto((-230, 270))
        self.write(f"Level = {self.level}", align=ALIGNMENT, font=("Courier", 15, "bold"))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
            self.goto(0, 0)
            self.color("black")
            self.write("Game Over", align=ALIGNMENT, font=("Courier", 20, "bold"))











