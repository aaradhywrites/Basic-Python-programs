import turtle
import math
import time
import random


screen = turtle.Screen()
screen.bgcolor("#000000")
screen.setup(width=1.0, height=1.0)

screen.cv._rootwindow.attributes("-fullscreen", True)
screen.cv._rootwindow.bind(
    "<Escape>",
    lambda e: screen.cv._rootwindow.attributes("-fullscreen", False)
)

screen.title("Line Rose ❄")
screen.tracer(1, 0)



t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

PETAL = "#e020dd"
LEAF = "#3fae55"
STEM = "#8a5a2e"
TITLE = "#e0203f"

Y = -60



def stroke(points, color, width=1.6, closed=True):
    t.pencolor(color)
    t.width(width)
    t.penup()
    t.goto(points[0])
    t.pendown()

    for p in points[1:]:
        t.goto(p)

    if closed:
        t.goto(points[0])

    t.penup()


def line(p1, p2, color, width=1.6):
    t.pencolor(color)
    t.width(width)
    t.penup()
    t.goto(p1)
    t.pendown()
    t.goto(p2)
    t.penup()



def stem_curve(x_amp, y0, y1, steps=50):
    pts = []

    for i in range(steps + 1):
        u = i / steps
        y = y0 + (y1 - y0) * u
        x = x_amp * math.sin(math.pi * 1.1 * u)
        pts.append((x, y))

    return pts


def draw_stem():
    pts = stem_curve(10, -300, Y)

    stroke(
        pts,
        STEM,
        width=2.2,
        closed=False
    )

    for u, side in [
        (0.22, 40),
        (0.5, -140),
        (0.76, 40)
    ]:
        i = int(u * (len(pts) - 1))

        x, y = pts[i]

        rad = math.radians(side)

        tip = (
            x + 12 * math.cos(rad),
            y + 12 * math.sin(rad)
        )

        line(
            (x, y),
            tip,
            STEM,
            width=1.3
        )


def leaf_points(length, width, steps=30):
    pts = []

    for i in range(steps + 1):
        u = i / steps

        x = length * u
        y = width * math.sin(math.pi * u) ** 0.7

        pts.append((x, y))

    for i in range(steps, -1, -1):
        u = i / steps

        x = length * u
        y = -width * math.sin(math.pi * u) ** 0.7

        pts.append((x, y))

    return pts


def draw_leaf(cx, cy, angle_deg, length, width):
    rad = math.radians(angle_deg)

    raw = leaf_points(
        length,
        width
    )

    pts = []

    for x, y in raw:

        px = (
            cx
            + x * math.cos(rad)
            - y * math.sin(rad)
        )

        py = (
            cy
            + x * math.sin(rad)
            + y * math.cos(rad)
        )

        pts.append((px, py))

    stroke(
        pts,
        LEAF,
        width=1.5
    )

    tip = (
        cx + length * 0.9 * math.cos(rad),
        cy + length * 0.9 * math.sin(rad)
    )

    line(
        (cx, cy),
        tip,
        LEAF,
        width=0.9
    )


def draw_stalked_leaf(
    base_x,
    base_y,
    angle_deg,
    scale=1.0
):

    rad = math.radians(angle_deg)

    stalk_len = 28 * scale

    tip = (
        base_x + stalk_len * math.cos(rad),
        base_y + stalk_len * math.sin(rad)
    )

    line(
        (base_x, base_y),
        tip,
        STEM,
        width=1.7
    )

    draw_leaf(
        tip[0],
        tip[1],
        angle_deg - 30,
        34 * scale,
        13 * scale
    )

    draw_leaf(
        tip[0],
        tip[1],
        angle_deg + 30,
        34 * scale,
        13 * scale
    )


def petal_points(
    length,
    half_width,
    steps=22,
    cap_steps=16
):

    body_len = length - half_width

    pts = [
        (0.0, 0.0)
    ]

    for i in range(1, steps + 1):

        u = i / steps

        x = body_len * u
        y = (
            half_width
            * math.sin(math.pi / 2 * u)
        )

        pts.append((x, y))

    for i in range(cap_steps + 1):

        a = 90 - 180 * i / cap_steps
        rad = math.radians(a)

        x = (
            body_len
            + half_width * math.cos(rad)
        )

        y = (
            half_width
            * math.sin(rad)
        )

        pts.append((x, y))

    for i in range(steps - 1, -1, -1):

        u = i / steps

        x = body_len * u

        y = (
            -half_width
            * math.sin(math.pi / 2 * u)
        )

        pts.append((x, y))

    return pts


def draw_petal(
    base_x,
    base_y,
    angle_deg,
    length,
    half_width,
    cup=0.0,
    width_line=1.6,
    midrib=False
):

    rad = math.radians(angle_deg)

    raw = petal_points(
        length,
        half_width
    )

    pts = []

    for x, y in raw:

        bend = (
            cup * (x / length) ** 2
            if length else 0
        )

        rx = (
            x * math.cos(rad)
            - (y + bend) * math.sin(rad)
        )

        ry = (
            x * math.sin(rad)
            + (y + bend) * math.cos(rad)
        )

        pts.append(
            (
                base_x + rx,
                base_y + ry
            )
        )

    stroke(
        pts,
        PETAL,
        width=width_line
    )

    if midrib:

        start = (
            base_x
            + length * 0.4 * math.cos(rad),
            base_y
            + length * 0.4 * math.sin(rad)
        )

        tip = (
            base_x
            + length * 0.88 * math.cos(rad),
            base_y
            + length * 0.88 * math.sin(rad)
        )

        line(
            start,
            tip,
            PETAL,
            width=max(
                0.6,
                width_line - 0.8
            )
        )



def spiral_points(
    cx,
    cy,
    turns,
    max_r,
    wiggle_amp,
    wiggle_freq,
    steps=220,
    start_r=3
):

    pts = []

    for i in range(steps + 1):

        u = i / steps

        theta = (
            u
            * turns
            * 2
            * math.pi
        )

        r = (
            start_r
            + (max_r - start_r) * u
        )

        r += (
            wiggle_amp
            * u
            * math.sin(
                theta * wiggle_freq
            )
        )

        x = (
            cx
            + r * math.cos(theta)
        )

        y = (
            cy
            + r * math.sin(theta)
        )

        pts.append((x, y))

    return pts


def petal_arc(
    cx,
    cy,
    a_start,
    a_end,
    r0,
    r_out,
    steps=44,
    taper=0.8
):

    pts = []

    for i in range(steps + 1):

        u = i / steps

        theta = math.radians(
            a_start
            + (a_end - a_start) * u
        )

        r = (
            r0
            + (r_out - r0)
            * math.sin(math.pi * u) ** taper
        )

        pts.append(
            (
                cx + r * math.cos(theta),
                cy + r * math.sin(theta)
            )
        )

    return pts




def draw_bloom():

    cx, cy = 0, Y + 70


    spiral = spiral_points(
        cx,
        cy,
        turns=2.5,
        max_r=42,
        wiggle_amp=5,
        wiggle_freq=4
    )

    stroke(
        spiral,
        PETAL,
        width=1.7,
        closed=False
    )

    screen.update()
    time.sleep(0.35)

    wraps = [
        (-20, 140, 34, 92, 2.1),
        (60, 230, 32, 100, 2.0),
        (150, 330, 30, 96, 2.0),
        (250, 420, 34, 88, 1.9),
        (10, 170, 36, 64, 1.4),
        (110, 260, 34, 60, 1.4)
    ]

    for (
        a_start,
        a_end,
        r0,
        r_out,
        w
    ) in wraps:

        pts = petal_arc(
            cx,
            cy,
            a_start,
            a_end,
            r0,
            r_out
        )

        stroke(
            pts,
            PETAL,
            width=w,
            closed=False
        )

        screen.update()
        time.sleep(0.1)

    
    outline = []

    n = 60

    for i in range(n + 1):

        a = 360 * i / n

        rad = math.radians(a)

        r = (
            100
            + 10 * math.sin(3 * rad)
            + 6 * math.sin(7 * rad + 1)
        )

        outline.append(
            (
                cx + r * math.cos(rad),
                cy + r * math.sin(rad)
            )
        )

    stroke(
        outline,
        PETAL,
        width=1.3
    )

draw_stem()

screen.update()
time.sleep(0.35)

draw_stalked_leaf(
    -6,
    -210,
    205,
    scale=1.1
)

screen.update()
time.sleep(0.2)

draw_stalked_leaf(
    5,
    -140,
    20,
    scale=0.9
)

screen.update()
time.sleep(0.2)

draw_stalked_leaf(
    -4,
    -260,
    160,
    scale=0.8
)

screen.update()
time.sleep(0.3)

draw_bloom()


# =========================
# TITLE
# =========================

t.pencolor(TITLE)
t.width(1)

t.goto(
    0,
    -460
)

t.write(
    "ROSE",
    align="center",
    font=("Georgia", 20, "normal")
)

screen.update()


snow = turtle.Turtle()

snow.hideturtle()
snow.penup()
snow.speed(0)

snowflakes = []



for i in range(100):

    x = random.randint(-750, 750)
    y = random.randint(-500, 500)

    
    size = random.choice([
        2,
        2,
        2,
        3,
        3,
        4
    ])

    
    speed = random.uniform(
        0.8,
        2.8
    )

    
    drift = random.uniform(
        -0.6,
        0.6
    )

    
    snowflakes.append([
        x,
        y,
        size,
        speed,
        drift
    ])




def draw_snow():

    snow.clear()

    for flake in snowflakes:

        x = flake[0]
        y = flake[1]
        size = flake[2]
        speed = flake[3]
        drift = flake[4]

    
        snow.goto(
            round(x),
            round(y)
        )

        snow.dot(
            size,
            "#349ecf"
        )


        flake[1] -= speed


        flake[0] += drift


        if flake[1] < -520:

            flake[0] = random.randint(
                -750,
                750
            )

            flake[1] = 520

            flake[2] = random.choice([
                2,
                2,
                3,
                4
            ])

            flake[3] = random.uniform(
                0.8,
                2.8
            )

        if flake[0] > 780:
            flake[0] = -780

        elif flake[0] < -780:
            flake[0] = 780


screen.tracer(0)


def animate():

    draw_snow()

    screen.update()

    # ~33 FPS
    screen.ontimer(
        animate,
        30
    )


animate()

screen.mainloop()