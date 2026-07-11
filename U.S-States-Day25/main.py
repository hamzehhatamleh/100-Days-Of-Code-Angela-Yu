import pandas as pd
import turtle

# 1. Screen Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

# 2. Turtle Setup (For writing names)
state_marker = turtle.Turtle()
state_marker.hideturtle()
state_marker.color("red")
state_marker.penup() 

# 3. Data Setup
Data_US = pd.read_csv("50_states.csv")
guessed_states = []

# 4. Game Loop
while len(guessed_states) < 50:
    # Gets input from popup and auto-corrects to title-case (e.g. "New York")
    user_input = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    # Break the loop safely if user clicks Cancel or types nothing
    if user_input is None:
        break

    user_input = user_input.title()

    # Secret exit keyword
    if user_input == "Exit":
        break

    # If the guess is correct and hasn't been guessed yet
    if user_input in Data_US['state'].values and user_input not in guessed_states:
        guessed_states.append(user_input)
        state = Data_US[Data_US.state == user_input]

        # Extract coordinates cleanly using .item()
        X = int(state['x'].item())
        Y = int(state['y'].item())

        # Move to position and write the name onto the map
        state_marker.goto(X, Y)
        state_marker.write(user_input, align="center", font=("Arial", 9, "bold"))

# 5. Keeps screen open dynamically
screen.mainloop()
