from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVING_DISTANCE = 20;
Up = 90;
Down = 270;
Right = 0;
Left = 180;

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segments(position)

    def add_segments(self, position):
        first_turtle = Turtle("square")
        first_turtle.color("white")
        first_turtle.penup()
        first_turtle.goto(position)
        self.segments.append(first_turtle)

    def increase_size(self):
        self.add_segments(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVING_DISTANCE)

    def Up(self):
        if self.head.heading() != Down:
           self.head.setheading(Up)

    def Down(self):
        if self.head.heading() != Up:
            self.segments[0].setheading(Down)

    def Right(self):
        if self.head.heading() != Left:
            self.segments[0].setheading(Right)

    def Left(self):
        if self.head.heading() != Right:
            self.segments[0].setheading(Left)