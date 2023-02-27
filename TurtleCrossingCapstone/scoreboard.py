from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 240)
        self.updatescoreboard()
    
    def increase(self):
        self.level += 1
        self.updatescoreboard()
    
    def updatescoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} ", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
