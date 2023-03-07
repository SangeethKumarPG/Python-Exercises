import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States")
img= "us-states-game/blank_states_img.gif"
screen.addshape(img)
correct_answers = 0
guessed_list = []
data = pandas.read_csv("us-states-game/50_states.csv")
turtle.shape(img)
while True:
    if correct_answers == 0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another states name?")
    else:
        answer_state = screen.textinput(title=f"{correct_answers}/50 correct", prompt="What's another states name?")

    answer_state = answer_state.title()
    # print(data)
    if answer_state == "Exit":
        break
    state_list = data["state"].to_list()
    if answer_state in state_list and answer_state not in guessed_list:
        state = data[data.state == answer_state]
        guessed_list.append(answer_state)
        # print(state)
        # print(int(state["x"]))
        x_cor = int(state["x"])
        y_cor = int(state["y"])
        correct_answers += 1
        pointer = turtle.Turtle()
        pointer.penup()
        pointer.hideturtle()
        pointer.goto(x_cor, y_cor)
        pointer.write(arg=f"{answer_state}", font=("Courier",10,"normal"))

states_to_learn = []
for state_name in state_list:
    if state_name not in guessed_list:
        states_to_learn.append(state_name)

# print(states_to_learn)
state_dict = {
    "state" : states_to_learn
}
data_frame = pandas.DataFrame(state_dict)
# print(data_frame)
data_frame.to_csv("us-states-game/learn.csv")



