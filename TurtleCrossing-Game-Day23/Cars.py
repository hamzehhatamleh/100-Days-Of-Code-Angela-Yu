from turtle import Turtle
import random

# --- CONSTANTS ---
CAR_WIDTH_STRETCH = 1
CAR_LENGTH_STRETCH = 1.5
CAR_HEADING_WEST = 180

# Spawn/Teleport Boundaries
MIN_LANE_Y = -240
MAX_LANE_Y = 240
LANE_STEP = 20

START_SPAWN_MIN_X = -280
START_SPAWN_MAX_X = 300
TELEPORT_MIN_X = 300
TELEPORT_MAX_X = 340
X_STEP = 10

RANDOM_COLORS = ["red", "green", "blue", "yellow", "orange", "pink", "gray"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(RANDOM_COLORS))
        self.penup()
        self.shapesize(stretch_wid=CAR_WIDTH_STRETCH, stretch_len=CAR_LENGTH_STRETCH, outline=None)
        self.left(CAR_HEADING_WEST)

        # Initial messy layout when the game first boots up
        initial_x = random.randrange(START_SPAWN_MIN_X, START_SPAWN_MAX_X, LANE_STEP)
        initial_y = random.randrange(MIN_LANE_Y, MAX_LANE_Y, LANE_STEP)
        self.goto(initial_x, initial_y)

    def TeleportCar(self):
        # Recycle the car back to the right side seamlessly without creating a new object
        self.hideturtle()
        self.goToRightEdge()
        self.showturtle()

    def goToRightEdge(self):
        random_x = random.randrange(TELEPORT_MIN_X, TELEPORT_MAX_X, X_STEP)
        random_y = random.randrange(MIN_LANE_Y, MAX_LANE_Y, LANE_STEP)
        self.goto(random_x, random_y)