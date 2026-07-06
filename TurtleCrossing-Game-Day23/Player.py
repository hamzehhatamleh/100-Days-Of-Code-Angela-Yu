from turtle import Turtle

# --- CONSTANTS ---
STARTING_X = 0
STARTING_Y = -280
MOVE_DISTANCE = 10
TURTLE_HEADING_NORTH = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(TURTLE_HEADING_NORTH)
        self.resetPos()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def resetPos(self):
        self.goto(STARTING_X, STARTING_Y)