from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
