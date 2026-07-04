import turtle as t

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SNAKE_SIZE = 20


class SnakeBody:
    def __init__(self):
        self.segments = []

        # Build starting snake at center (0,0) growing left
        for i in range(3):
            self.addSegment()
            self.segments[i].goto(i * -SNAKE_SIZE, 0)
            self.segments[i].showturtle()

        self.head = self.segments[0]

    def addSegment(self):
        new_segment = t.Turtle()
        new_segment.hideturtle()  # Stop the visual flash bug
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.shapesize(1, 1)

        # Place the new segment exactly where the current tail is
        if len(self.segments) > 0:
            tail_x = self.segments[-1].xcor()
            tail_y = self.segments[-1].ycor()
            new_segment.goto(tail_x, tail_y)
            new_segment.showturtle()

        self.segments.append(new_segment)

    def move(self):
        # Move segments from back to front
        for num in range(len(self.segments) - 1, 0, -1):
            x_prev = self.segments[num - 1].xcor()
            y_prev = self.segments[num - 1].ycor()
            self.segments[num].goto(x_prev, y_prev)

        self.head.forward(SNAKE_SIZE)

    def moveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
