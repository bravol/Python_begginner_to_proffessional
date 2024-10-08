from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        # left score
        self.goto(-100,200)
        self.write(self.left_score, align='center', font=("Courier", 80, "normal"))
        # right score
        self.goto(100,200)
        self.write(self.right_score, align='center', font=("Courier", 80, "normal"))

    def increase_left_point(self):
        self.left_score += 1
        self.update_score_board()

    def increase_right_point(self):
        self.right_score += 1
        self.update_score_board()