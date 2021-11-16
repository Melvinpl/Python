from turtle import Turtle
FONT = ('Arial',20,"normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-60,280)
        self.color("white")
        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score : {self.score}" ,move=False, font=FONT)
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", move=False, font=FONT)