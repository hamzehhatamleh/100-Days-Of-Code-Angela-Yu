import turtle
import time
import Player
import Level
import Cars

# --- CONSTANTS (Configuration) ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GAME_LOOP_DELAY = 0.01
START_CAR_COUNT = 20

# Collision Padding
HITBOX_WIDTH_LIMIT = 20
HITBOX_HEIGHT_LIMIT = 21

# Boundaries
LEFT_SCREEN_BOUNDARY = -320
WINNING_Y_LINE = 280

# --- SETUP ---
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

player = Player.Player()
all_cars = []
level = Level.Level()

screen.listen()
screen.onkey(player.move, "Up")

# Spawn initial car pool
for _ in range(START_CAR_COUNT):
    car = Cars.Car()
    all_cars.append(car)

game_is_on = True

# --- MAIN GAME LOOP ---
while game_is_on:
    screen.update()
    time.sleep(GAME_LOOP_DELAY)

    for car in all_cars:
        car.forward(level.game_speed)

        # 1. Calculate precise distance on X and Y axes separately
        x_distance = abs(car.xcor() - player.xcor())
        y_distance = abs(car.ycor() - player.ycor())

        # 2. Apply custom hit-box rule using constants
        if x_distance < HITBOX_WIDTH_LIMIT and y_distance < HITBOX_HEIGHT_LIMIT:
            level.GameOver()
            game_is_on = False

        # 3. Check if the car needs to loop back to the right side
        if car.xcor() < LEFT_SCREEN_BOUNDARY:
            car.TeleportCar()

    # 4. Check Win Condition
    if player.ycor() >= WINNING_Y_LINE:
        player.resetPos()
        level.increaseLevel()

screen.exitonclick()