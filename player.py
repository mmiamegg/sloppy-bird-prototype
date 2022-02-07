from turtle import Turtle

SHAPE = "circle"
COLOR = "black"
JUMP_DISTANCE = 20
MOVE_DISTANCE = 15



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.turtlesize(3)
        self.color(COLOR)
        self.penup()
        self.setposition((-300, 0))

    def fall(self):
        # new_ycor = self.ycor() - MOVE_DISTANCE
        # self.goto(x=-350, y=new_ycor)
        self.setheading(90)
        self.backward(MOVE_DISTANCE)

    def jump(self):
        self.setheading(90)
        for num in range(3):
            self.forward(JUMP_DISTANCE)
