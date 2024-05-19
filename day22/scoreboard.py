from turtle import Turtle
Y_COORD = 275

class Scoreboard(Turtle):
    l_SCORE = 0
    r_SCORE = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=-10, y=Y_COORD)
        self.write(f"{self.l_SCORE} : {self.r_SCORE} ",align="center",font=("Arial",16,"normal"))

    def add_score(self, player_score):
        self.clear()
        if player_score == "l_SCORE":
            self.l_SCORE += 1
        elif player_score == "r_SCORE":
            self.r_SCORE += 1
        self.__init__()

    def game_over(self):
        if self.l_SCORE == 3 or self.r_SCORE == 3:
            self.goto(0, 0)
            self.write("GAME OVER",align="center",font=("Arial",16,"normal"))
            return False
        else:
            return True

if __name__ == '__main__':
    src = Scoreboard()
    src.add_score()
    src.add_score()
    src.add_score()
    print(Scoreboard.SCORE)

