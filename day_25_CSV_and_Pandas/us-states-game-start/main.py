import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S.  States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
result_text = turtle.Turtle()
result_text.penup()
result_text.hideturtle()


def get_mouse_click_coor(x, y):
    print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

# track wright guesses
wright_guesses = ["" for x in range(50)]

df = pd.read_csv("50_states.csv")
states = df.state.to_list()


def write_state(df, guess):
    coor_x = float(df.x[df.state == guess])
    coor_y = float(df.y[df.state == guess])
    result_text.goto(coor_x, coor_y)
    result_text.write(guess)


# loop game until the 50 states are guessed
while "" in wright_guesses:
    try:
        answer_state = screen.textinput(title=f"{len(wright_guesses)}/50 States Correct",
                                        prompt="what's another state's "
                                               "name?").title().strip()
    except AttributeError:
        break

    if answer_state == "Exit":
        break

    if answer_state in states:
        wright_guesses.remove("")
        wright_guesses.insert(0, answer_state)
        write_state(df, answer_state)

turtle.mainloop()

# states_to_learn.csv

states_to_learn = [x for x in states if x not in wright_guesses]
while len(states_to_learn) < 50:
    states_to_learn.append("")

states_to_learn = {
    "States to learn": states_to_learn,
    "Wright answers": wright_guesses

}

print(states_to_learn)

df_to_learn = pd.DataFrame(states_to_learn)
df_to_learn.to_csv("states_to_learn.csv")
print("file written")
print(df_to_learn)
