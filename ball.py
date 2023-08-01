import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def y_bounce(self):
        """Changing y direction when bouncing"""
        self.y_move *= -1

    def x_bounce(self):
        """Changing x direction when bouncing, and increasing the speed"""
        self.x_move *= -1
        self.move_speed *= 0.9


    def move(self):
        current_x = self.xcor() + self.x_move
        current_y = self.ycor() + self.y_move
        self.goto(current_x, current_y)

    def reset_position(self):
        self.setposition(0, 0)
        # Reset the ball speed at its initial value
        self.move_speed = 0.1
        self.x_bounce()


