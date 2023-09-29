from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


score=Scoreboard();

screen = Screen()
food = Food()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
segments = []

initial_position = [(0,0), (-20,0), (-40,0)]

snake = Snake()
screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Right, "Right")
screen.onkey(snake.Left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


#----------------------------detecting collision with food------------------------------#

    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.increase_size()
#----------------------------------------------------------------------------------------#

    if snake.head.xcor()>299 or snake.head.xcor()<-299 or snake.head.ycor()>299 or snake.head.ycor()<-299:
        game_is_on = False
        score.game_end()

    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_end()

screen.exitonclick()
