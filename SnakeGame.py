import turtle as t
import SnakeBody
import time
from Food import Food
from Score import Score

COLLISION_DISTANCE = 15

# Set up screen
screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("white") # Optional: explicit background color
screen.tracer(0)

# Calculate boundaries dynamically based on screen size (300 - 20 padding = 280)
WALL_LIMIT = (screen.window_width() / 2) - 20

# Initialize objects
Snake = SnakeBody.SnakeBody()
food_item = Food()
score = Score()

# Keyboard bindings
screen.listen()
screen.onkey(fun=Snake.moveUp, key="Up")
screen.onkey(fun=Snake.moveDown, key="Down")
screen.onkey(fun=Snake.moveLeft, key="Left")
screen.onkey(fun=Snake.moveRight, key="Right")

game_is_on = True

while game_is_on:
    Snake.move()

    # 1. Food Collision
    if Snake.head.distance(food_item) < COLLISION_DISTANCE:
        score.increase()
        Snake.addSegment()
        food_item.regenerate()

    # 2. Wall Collision (Dynamic boundary checking)
    if (abs(Snake.head.xcor()) > WALL_LIMIT or
        abs(Snake.head.ycor()) > WALL_LIMIT):
        score.game_over()
        game_is_on = False

    # 3. Tail Collision (Slices out the head at index 0)
    for segment in Snake.segments[1:]:
        if Snake.head.distance(segment) < COLLISION_DISTANCE:
            score.game_over()
            game_is_on = False

    screen.update()
    time.sleep(0.1)

# Safely wait for click to exit without console errors
screen.exitonclick()
