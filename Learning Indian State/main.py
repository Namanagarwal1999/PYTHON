import turtle

import pandas
screen = turtle.Screen()
screen.title("India States Game")
image = "blank_states.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

input_list = []
score = 0
data = pandas.read_csv("28_states.csv")
state_list = data["state"].to_list()
username = screen.textinput(title="Username", prompt="What is your name?")
while len(input_list) < 28:
    print (input_list)
    print (len(input_list))
    answer_state = screen.textinput(title=f"{score}/28 States correct", prompt="What's another state's name?")
    titlecase_answer_state = answer_state.title()
    # input_list.append(titlecase_answer_state)
    if titlecase_answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in input_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(f"states_to_learn({username}).csv")

        break

    for state in state_list:
        if state == titlecase_answer_state:
            score += 1
            input_list.append(titlecase_answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            guess_state_data =data[data.state == (state)]
            x_cor = int(guess_state_data.x)
            y_cor = int(guess_state_data.y)
            t.goto(x_cor, y_cor)
            t.write(state)

states_to_learn.csv
states_to_learn = [i for i in state_list if i not in input_list]
print(states_to_learn)


# screen.exitonclick()
