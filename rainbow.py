import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)
screen.tracer(0)

pen = turtle.Turtle()

def semi_circle(col, rad, val):
    pen.color(col)
    pen.circle(rad, -180)
    pen.up()
    pen.setpos(val, 0)
    pen.down()
    pen.right(180)

raindrops = []
NUM_RAINDROPS = 100

def create_raindrops():
    for _ in range(NUM_RAINDROPS):
        raindrop = turtle.Turtle()
        raindrop.shape("circle")
        raindrop.color("blue")
        raindrop.penup()
        raindrop.speed(0)
        raindrop.shapesize(stretch_wid=0.3, stretch_len=0.3)
        raindrop.setposition(random.randint(-400, 400), random.randint(200, 600))
        raindrops.append(raindrop)

def update_raindrops():
    for raindrop in raindrops:
        raindrop.sety(raindrop.ycor() - 5)
        if raindrop.ycor() < -300:
            raindrop.setposition(random.randint(-400, 400), random.randint(200, 600))

def draw_sun():
    sun = turtle.Turtle()
    sun.penup()
    sun.goto(-200, 200)
    sun.pendown()
    sun.color("yellow")
    sun.begin_fill()
    sun.circle(50)
    sun.end_fill()
    for _ in range(12):
        sun.penup()
        sun.goto(-200, 250)
        sun.pendown()
        sun.forward(70)
        sun.penup()
        sun.goto(-200, 250)
        sun.right(30)
    sun.hideturtle()

col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
screen.setup(600, 600)
pen.right(90)
pen.width(10)
pen.speed(7)
draw_sun()

def rain_effect():
    create_raindrops()
    start_time = time.time()
    while time.time() - start_time < 6:
        update_raindrops()
        screen.update()
    for raindrop in raindrops:
        raindrop.hideturtle()
    for i in range(7):
        semi_circle(col[i], 10*(i + 8), -10*(i + 1))
    # screen.update()
    create_raindrops()
    start_time = time.time()
    while time.time() - start_time < 6:
        update_raindrops()
        screen.update()

rain_effect()
pen.hideturtle()
turtle.done()
