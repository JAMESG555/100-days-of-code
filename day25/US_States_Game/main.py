import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
correct_states=[]

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state =="Exit":
        learn_list = []
        for s in all_states:
            if s not in correct_states:
                learn_list.append(s)
        new_data = pandas.DataFrame(learn_list)
        new_data.to_csv("states_to_learn.csv")

    if answer_state in all_states and answer_state not in correct_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.speed("fastest")
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_states.append(answer_state)

# states_to_learn.csv

screen.exitonclick()



