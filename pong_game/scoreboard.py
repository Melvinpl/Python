from turtle import Turtle, update
FONT = ('Arial',20,"normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-60,280)
        self.write(self.l_score,align="center", font=FONT)
        self.goto(60,280)
        self.write(self.r_score,align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()