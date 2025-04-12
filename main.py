from turtle import Turtle, Screen
import pandas

ALIGNMENT = "center"
FONT = ("Verdana", 7, "normal")

screen = Screen()
t = Turtle()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data["state"].to_list()  # list of states names
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                             prompt="What's another state name?").title()
    matching_row = states_data[states_data["state"] == guess]

    if guess in all_states and guess not in guessed_states:
        guessed_states.append(guess)
        # Create country name on screen
        country = Turtle()
        country.penup()
        country.hideturtle()
        print(matching_row.x.item())
        country.goto(matching_row.x.item(), matching_row.y.item())
        country.write(matching_row["state"].item(), align=ALIGNMENT, font=FONT)

    elif guess == "Exit":
        break

# Save missing states to csv file
list_to_learn = [state for state in all_states if state not in guessed_states]
df = pandas.DataFrame(list_to_learn)
df.to_csv("states_to_learn.csv")