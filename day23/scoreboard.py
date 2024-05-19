from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    SCORE = 0

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-240, y=260)
        self.write(f"Level: {self.SCORE} ", align="center", font=("Arial", 16, "normal"))

    def add_score(self):
        self.clear()
        self.SCORE += 1
        self.__init__()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center",font=("Arial",16,"normal"))
        return False
