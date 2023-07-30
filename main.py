import time
from turtle import Screen

from ball import Ball
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball((0, 0))

### CONTROLING THE SNAKE ###
# Listening to the keys tapped

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="a")
screen.onkey(fun=l_paddle.down, key="q")

is_game_on = True
# Move the segments forward
while is_game_on:
    time.sleep(0.1)
    # Update the screen before the paddle moves. This way, it'll appear as a paddle moving
    screen.update()
    ball.move()

screen.exitonclick()


