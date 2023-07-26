from turtle import Turtle

FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-285, 275)
        self.write(f"Level: {self.current_level}", align='left', font=(FONT))

    def new_level(self):
        self.current_level += 1
        self.update_scoreboard()

    def final_scores(self):
        self.clear()
        self.goto(0, 0)
        self.color('red')
        self.write(f"  GAME ENDED\nFinal Level: {self.current_level}", align='center', font=("Courier", 25, "bold"))