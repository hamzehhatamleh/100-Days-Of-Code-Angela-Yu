import turtle as t

# --- CONSTANTS ---
TEXT_X_COR = -230
TEXT_Y_COR = 260
CENTER_X = 0
CENTER_Y = 0

FONT_NAME = "Arial"
FONT_SIZE_SCORE = 16
FONT_SIZE_GAME_OVER = 24
FONT_STYLE = "bold"

STARTING_SPEED = 0.7
SPEED_INCREMENT = 0.2

class Level:
    def __init__(self):
        self.writer = t.Turtle()
        self.writer.hideturtle()
        self.writer.color("black")
        self.writer.penup()
        self.writer.goto(TEXT_X_COR, TEXT_Y_COR)

        self.level = 1
        self.game_speed = STARTING_SPEED
        self.updateWrite()

    def increaseGameSpeed(self):
        self.game_speed += SPEED_INCREMENT

    def updateWrite(self):
        self.writer.clear()
        self.writer.write(f"Level: {self.level}", align="center", font=(FONT_NAME, FONT_SIZE_SCORE, FONT_STYLE))

    def GameOver(self):
        self.writer.clear()
        self.writer.goto(CENTER_X, CENTER_Y)
        self.writer.write("Game Over", align="center", font=(FONT_NAME, FONT_SIZE_GAME_OVER, FONT_STYLE))

    def increaseLevel(self):
        self.level += 1
        self.increaseGameSpeed()
        self.updateWrite()