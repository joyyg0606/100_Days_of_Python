import pandas, turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "CSV Data & Pandas Library/US States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("CSV Data & Pandas Library/US States Game/50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="Enter a state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        data = pandas.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        current_state_data = data[data.state == answer_state]
        text.goto(int(current_state_data.x), int(current_state_data.y))
        text.write(answer_state, align='center')