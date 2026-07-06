from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        # Initialize the parent Turtle class
        super().__init__()

        # Style and place the paddle
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)  # 5 high, 1 wide standard Pong size
        self.goto(position)

    def move_up(self):
        """Moves the paddle up until it hits the screen boundary."""
        current_y = self.ycor()
        if current_y <= 240:
            self.sety(current_y + 20)

    def move_down(self):
        """Moves the paddle down until it hits the screen boundary."""
        current_y = self.ycor()
        if current_y >= -240:
            self.sety(current_y - 20)