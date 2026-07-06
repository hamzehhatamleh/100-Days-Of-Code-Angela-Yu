from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 6
        self.move_speed = 0.04 # Start with your current speed delay

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # Every time it hits a paddle, slice 10% off the delay time to speed it up!
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.04 # Reset back to the normal starting speed
        self.bounce_x()