from turtle import Turtle

# CONSTANTS
ALIGNMENT = 'center'
ARIAL = 'Arial'
NORMAL = 'normal'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.write(f"Score {self.score}", align=ALIGNMENT, font=(ARIAL, 24,NORMAL))


    def increase_score(self):
        self.score += 1
        self.clear() # clear the score board that was written before
        self.update_score_board()


