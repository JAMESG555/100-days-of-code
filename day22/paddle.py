from turtle import Turtle


class Paddle(Turtle):


    def __init__(self, x_pos):
        super().__init__()
        x_position = {
            "left_x": -350,
            "right_x": 350
        }
        y_pos = 0
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_position[x_pos], y_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)