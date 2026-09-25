import turtle
import math
import time

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.colormode(1.0)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(1)

# Soothing blue
bright = (0.02, 0.70, 0.85)
dark = (0.00, 0.15, 0.25)


# ---------------- MOON ----------------
def moon_point(angle, radius):
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    return x, y


def draw_moon():
    # Draw moon using many circular strokes
    for r in range(55, 3, -2):

        t.penup()

        x, y = moon_point(0, r)
        t.goto(x, y + 150)

        t.pendown()

        for a in range(0, 361, 4):
            angle = math.radians(a)

            x, y = moon_point(angle, r)

            # Crescent shape
            if x < 18:
                t.goto(x, y + 150)

        screen.update()


# ---------------- RIVER ----------------
def draw_river():
    # Several flowing lines make the river
    for row in range(18):

        y = -180 - row * 8

        t.penup()
        t.goto(-300, y)
        t.pendown()

        for x in range(-300, 301, 4):

            wave = math.sin(x * 0.035 + row * 0.4) * 4

            # Colour gradient
            f = row / 18
            col = tuple(
                bright[c] + (dark[c] - bright[c]) * f
                for c in range(3)
            )

            t.pencolor(col)
            t.goto(x, y + wave)

        screen.update()


# ---------------- FALLING MOON ----------------
def falling_moon(start_y, end_y):

    # Clear only the moon area before redrawing
    for y in range(start_y, end_y, -2):

        # Redraw moon at new position
        radius = 48

        t.penup()
        t.goto(radius, y)
        t.pendown()

        t.pencolor(bright)

        for a in range(0, 361, 5):

            angle = math.radians(a)

            x = radius * math.cos(angle)
            yy = radius * math.sin(angle)

            # Crescent
            if x < 16:
                t.goto(x, yy + y)

        screen.update()
        time.sleep(0.025)


# ==================================================
# 1. CREATE MOON
# ==================================================

draw_moon()

time.sleep(1)


# ==================================================
# 2. CREATE RIVER
# ==================================================

draw_river()

time.sleep(1)


# ==================================================
# 3. MOON FALLS
# ==================================================

# Falling animation
for y in range(150, -150, -2):

    # Redraw the entire scene so the old moon disappears
    t.clear()

    # Moon at current position
    radius = 50

    t.penup()
    t.goto(0, y)
    t.pendown()

    t.pencolor(bright)

    for a in range(0, 361, 4):

        angle = math.radians(a)

        x = radius * math.cos(angle)
        yy = radius * math.sin(angle)

        if x < 15:
            t.goto(x, yy + y)

    # River stays at bottom
    for row in range(18):

        ry = -180 - row * 8

        t.penup()
        t.goto(-300, ry)
        t.pendown()

        for x in range(-300, 301, 5):

            wave = math.sin(x * 0.035 + row * 0.4) * 4

            f = row / 18

            col = tuple(
                bright[c] + (dark[c] - bright[c]) * f
                for c in range(3)
            )

            t.pencolor(col)
            t.goto(x, ry + wave)

    screen.update()
    time.sleep(0.02)


# ==================================================
# 4. MOON SUBMERGES
# ==================================================

for y in range(-150, -230, -2):

    t.clear()

    # River
    for row in range(18):

        ry = -180 - row * 8

        t.penup()
        t.goto(-300, ry)
        t.pendown()

        for x in range(-300, 301, 5):

            wave = math.sin(x * 0.035 + row * 0.4) * 4

            f = row / 18

            col = tuple(
                bright[c] + (dark[c] - bright[c]) * f
                for c in range(3)
            )

            t.pencolor(col)
            t.goto(x, ry + wave)

    # Moon
    radius = 50

    t.penup()
    t.goto(0, y)
    t.pendown()

    t.pencolor(bright)

    for a in range(0, 361, 4):

        angle = math.radians(a)

        x = radius * math.cos(angle)
        yy = radius * math.sin(angle)

        if x < 15:
            t.goto(x, yy + y)

    screen.update()
    time.sleep(0.025)


# ---------------- FINAL RIPPLE ----------------

t.clear()

for size in range(5, 150, 3):

    t.penup()
    t.goto(size, -180)
    t.setheading(90)
    t.pendown()

    t.pencolor(bright)

    t.circle(size)

    screen.update()
    time.sleep(0.02)

turtle.done()