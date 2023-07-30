from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(position)

    def move(self):
        # current_x = self.xcor() + 10
        # current_y = self.ycor() + 10
        #self.goto(current_x, current_y)
        current_x, current_y = self.position()
        has_reached_edge = False
        while has_reached_edge:
            new_x = current_x + 10
            new_y = current_y + 10

            if new_y < 300:
                new_x = current_x + 10
                new_y = current_y + 10
            elif current_y == 300:
                new_x = current_x + 10
                new_y = self.ycor() - 10
                has_reached_edge = True
            elif current_y == -300:
                new_x = current_x + 10
                new_y = self.ycor() + 10
                has_reached_edge = True
            else:
                new_x = current_x + 10
                new_y = self.ycor() + 10
            self.goto(new_x, new_y)