import random
from turtle import Turtle

OBSTACLE_SPEED = 10
MAX_PILLAR_HEIGHT = 8

class PillarObstacle:
    def __init__(self):
        self.bottom_pillars = []
        self.top_pillars = []
        self.move_speed = OBSTACLE_SPEED
        self.pillar_x_position = 600

    # create bottom obstacles on screen
    def create_bottom_pillar(self):
        random_chance = random.randint(1, 4)
        if random_chance == 3:
            pass
        else:
            pillar_height = self.random_height()
            new_pillar = Turtle()
            new_pillar.shape("square")
            new_pillar.color("black")
            new_pillar.penup()
            new_pillar.shapesize(stretch_wid=pillar_height, stretch_len=5)
            new_pillar.setposition((self.pillar_x_position, self.compute_bottom_pillar_ycor(pillar_height)))
            self.bottom_pillars.append(new_pillar)
            self.create_top_pillar()

    # create top obstacles on screen
    def create_top_pillar(self):
        pillar_height = self.random_height()
        new_pillar = Turtle()
        new_pillar.shape("square")
        new_pillar.color("black")
        new_pillar.penup()
        new_pillar.shapesize(stretch_wid=pillar_height, stretch_len=5)
        new_pillar.setposition((self.pillar_x_position, self.compute_top_pillar_ycor(pillar_height)))
        self.top_pillars.append(new_pillar)

    # compute for the bottom pillar's y coordinate based on the pillar's height
    def compute_bottom_pillar_ycor(self, pillar_height):
        compute = (pillar_height * 20) / 2
        new_height = compute - 250
        return new_height

    # compute for the top pillar's y coordinate based on the pillar's height
    def compute_top_pillar_ycor(self, pillar_height):
        compute = (pillar_height * 20) / 2 * -1
        new_height = compute + 250
        return new_height

    # give a pillar a random height
    def random_height(self):
        return random.randint(2, MAX_PILLAR_HEIGHT)

    def move_pillars(self):
        for bottom_pillar in self.bottom_pillars:
            bottom_pillar.backward(self.move_speed)
        for top_pillar in self.top_pillars:
            top_pillar.backward(self.move_speed)

