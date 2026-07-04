import turtle as t

class Score:
    def __init__(self):
        self.current_score = 0  # Renamed to avoid confusion with class name

        self.writer = t.Turtle()
        self.writer.color("black")
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.goto(0, 260)

        self.update_display()

    def update_display(self):
        self.writer.clear()
        self.writer.write(f"Score: {self.current_score}", align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.writer.goto(0, 0)
        self.writer.write("GAME OVER !", align="center", font=("Arial", 24, "bold"))

    def increase(self):
        self.current_score += 1
        self.update_display()
