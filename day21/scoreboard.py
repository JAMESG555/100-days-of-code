from turtle import Turtle
Y_COORD = 275

class Scoreboard(Turtle):
    SCORE = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=-10, y=Y_COORD)
        self.write(f"score : {self.SCORE} ",align="center",font=("Arial",16,"normal"))

    def add_score(self):
        self.clear()
        Scoreboard.SCORE += 1
        self.__init__()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center",font=("Arial",16,"normal"))


if __name__ == '__main__':
    src = Scoreboard()
    src.add_score()
    src.add_score()
    src.add_score()
    print(Scoreboard.SCORE)

