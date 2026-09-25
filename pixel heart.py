import turtle
import math

def heart(t):
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x, y

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.colormode(1.0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(1)

N, K = 140, 2.1
SCALE = 10

# Soothing blue color
bright, dark = (0.02, 0.70, 0.85), (0.00, 0.20, 0.30)

for i in range(N):
    ang = 2 * math.pi * i / N
    hx, hy = heart(ang)
    hx, hy = hx * SCALE, hy * SCALE
    ex, ey = hx * K, hy * K
    steps = 14

    t.penup()
    t.goto(hx, hy)
    t.pendown()

    for j in range(steps):
        f = (j + 1) / steps
        col = tuple(
            bright[c] + (dark[c] - bright[c]) * f
            for c in range(3)
        )
        t.pencolor(col)
        t.goto(
            hx + (ex - hx) * f,
            hy + (ey - hy) * f
        )

turtle.done()