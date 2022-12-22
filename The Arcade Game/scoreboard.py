from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto((-150, 250))
        self.write(f" Player 1 \n Score = {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto((150, 250))
        self.write(f" Player 2 \n Score = {self.r_score}", align=ALIGNMENT, font=FONT)


    def increase_score_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_score_r(self):
        self.r_score += 1
        self.update_scoreboard()

    def player1_win(self):
            self.goto(0, 0)
            self.write(f"   Game Over \n Player 1 wins", align=ALIGNMENT, font=("Courier", 20, "bold"))

    def player2_win(self):
            self.goto(0, 0)
            self.write(f"   Game Over \n Player 2 wins", align=ALIGNMENT, font=("Courier", 20, "bold"))









