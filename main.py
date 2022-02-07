import time
from turtle import Screen
from player import Player
from pillar_obstacles import PillarObstacle

screen = Screen()
screen.setup(width=900, height=600)
screen.title("Floppy Bird Prototype")
screen.tracer(0)

player = Player()
obstacles = PillarObstacle()

screen.listen()
screen.onkey(player.jump, "space")

game_is_on = True
countdown = 11
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # generate pillars
    if countdown == 10:
        obstacles.create_bottom_pillar()
    if countdown == 0:
        countdown = 11
    countdown -= 1
    obstacles.move_pillars()

    # move ball
    player.fall()

    for p in obstacles.top_pillars:
        size = [s for s in p.shapesize()]
        p_bottom_height = p.ycor() - (size[0] * 10)
        player_top_height = player.ycor() + 20
        
        if p.xcor() >= -320 and p.xcor() <= -230:
            if player_top_height >= p_bottom_height:
                game_is_on = False

    for p in obstacles.bottom_pillars:
        size = [s for s in p.shapesize()]
        p_top_height = p.ycor() + (size[0] * 10)
        player_bottom_height = player.ycor() - 20

        if p.xcor() >= -320 and p.xcor() <= -230:
            if player_bottom_height <= p_top_height:
                game_is_on = False


screen.exitonclick()
