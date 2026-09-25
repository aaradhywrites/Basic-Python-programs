import turtle
import math
import time

screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor("#061526")
screen.title("Falling Moon 🌙")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

moon = turtle.Turtle()
moon.hideturtle()
moon.speed(0)

river = turtle.Turtle()
river.hideturtle()
river.speed(0)

stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)

ripple = turtle.Turtle()
ripple.hideturtle()
ripple.speed(0)


def rectangle(t, x1, y1, x2, y2, color):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()


def draw_river():
    rectangle(
        river,
        -400, -350,
        400, -80,
        "#073B4C"
    )

    river.color("#0B6075")
    river.width(2)

    for y in range(-100, -340, -25):
        river.penup()
        river.goto(-380, y)

        river.pendown()

        for x in range(-380, 381, 20):
            wave = math.sin(x * 0.04) * 3
            river.goto(x, y + wave)


def draw_stars():
    stars.color("#DDF7FF")

    star_positions = [
        (-330, 270), (-250, 220), (-170, 290),
        (-70, 245), (30, 300), (130, 250),
        (220, 285), (320, 230),
        (-300, 160), (-150, 180), (60, 170),
        (200, 150), (340, 180)
    ]

    for x, y in star_positions:
        stars.penup()
        stars.goto(x, y)
        stars.dot(3)


def draw_moon(x, y, radius=65):
    moon.clear()

    moon.penup()
    moon.goto(x, y - radius)
    moon.pendown()

    moon.fillcolor("#DDF6FF")
    moon.color("#DDF6FF")

    moon.begin_fill()
    moon.circle(radius)
    moon.end_fill()

    moon.penup()
    moon.goto(x + 25, y - radius + 12)
    moon.pendown()

    moon.fillcolor("#061526")
    moon.color("#061526")

    moon.begin_fill()
    moon.circle(radius - 5)
    moon.end_fill()


def draw_ripple(x, y, size):
    ripple.clear()

    ripple.color("#45CDE8")
    ripple.width(2)

    ripple.penup()
    ripple.goto(x + size, y)
    ripple.setheading(90)
    ripple.pendown()

    ripple.circle(size)


draw_stars()
draw_river()

moon_x = 0
moon_y = 210

draw_moon(moon_x, moon_y)

screen.update()
time.sleep(2)



for y in range(210, -75, -2):

    draw_moon(moon_x, y)

    screen.update()
    time.sleep(0.025)



draw_moon(moon_x, -75)
screen.update()
time.sleep(0.4)


for y in range(-75, -150, -2):

    draw_moon(moon_x, y)

    rectangle(
        river,
        -400, -80,
        400, -350,
        "#073B4C"
    )


    river.color("#0B6075")
    river.width(2)

    for ry in range(-100, -340, 30):
        river.penup()
        river.goto(-380, ry)
        river.pendown()

        for x in range(-380, 381, 25):
            wave = math.sin(x * 0.04) * 3
            river.goto(x, ry + wave)

    screen.update()
    time.sleep(0.025)


moon.clear()

for size in range(10, 180, 5):
    draw_ripple(0, -82, size)

    screen.update()
    time.sleep(0.025)

ripple.clear()
screen.update()

# Keep final peaceful scene
time.sleep(3)

turtle.done()