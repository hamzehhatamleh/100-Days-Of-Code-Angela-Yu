import turtle
import time
from Paddle import Paddle
from Ball import Ball
from Score import ScoreBoard

# Screen Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

# Turn off animations so drawings load instantly
screen.tracer(0)

# Spawn Game Objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
sb = ScoreBoard()

# Setup keyboard listening connections
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

# Main Game Loop
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed) # Dynamically changes now!
    screen.update()
    ball.move()
    # Detect ceiling and floor collisions
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Right Paddle Collision (Only bounce if ball is moving RIGHT towards it)
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        if ball.x_move > 0:
            ball.bounce_x()

    # Left Paddle Collision (Only bounce if ball is moving LEFT towards it)
    if ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        if ball.x_move < 0:
            ball.bounce_x()

    # Detect when Right Paddle misses
    if ball.xcor() > 390:
        ball.reset_pos()
        sb.increase_left_score()

    # Detect when Left Paddle misses
    if ball.xcor() < -390:
        ball.reset_pos()
        sb.increase_right_score()

# Keep window open cleanly if loop breaks
screen.exitonclick()