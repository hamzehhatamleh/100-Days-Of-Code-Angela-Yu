from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()

        # Draw the permanent center line static elements once on startup
        self.draw_center_line()
        self.update_score()

    def draw_center_line(self):
        """Draws the retro dashed line down the middle once."""
        line_drawer = Turtle()
        line_drawer.hideturtle()
        line_drawer.color("white")
        line_drawer.penup()
        line_drawer.shape("square")
        line_drawer.shapesize(stretch_wid=0.5, stretch_len=0.5)

        # Stamp the squares only once so it doesn't leak memory mid-game
        for i in range(380, -380, -30):
            line_drawer.goto(0, i)
            line_drawer.stamp()

    def update_score(self):
        """Refreshes the score display text."""
        self.clear()

        # 1. Draw Left Score
        self.goto(-100, 220)
        self.write(self.left_score, align="center", font=("Courier", 50, "normal"))

        # 2. Draw Right Score
        self.goto(100, 220)
        self.write(self.right_score, align="center", font=("Courier", 50, "normal"))

    def increase_left_score(self):
        self.left_score += 1
        self.update_score()

    def increase_right_score(self):
        self.right_score += 1
        self.update_score()