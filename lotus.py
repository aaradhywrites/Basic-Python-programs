import turtle
import math
import time

# =========================================================
# FULLSCREEN SETUP
# =========================================================

screen = turtle.Screen()
screen.bgcolor("#061b2b")
screen.setup(width=1.0, height=1.0)
screen.cv._rootwindow.attributes("-fullscreen", True)

# ESC = exit fullscreen
screen.cv._rootwindow.bind(
    "<Escape>",
    lambda e: screen.cv._rootwindow.attributes("-fullscreen", False)
)

screen.title("Growing Lotus")
screen.tracer(1, 0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

# =========================================================
# COLORS
# =========================================================

WATER = "#0EBDBD"
WATER_LINE = "#083775"

STEM = "#1f6b42"
STEM_LIGHT = "#4ca866"

LEAF = "#176b4a"
LEAF_LIGHT = "#3d9b65"

OUTER = "#c1305f"
OUTER_EDGE = "#8f1f45"
MIDDLE = "#e0507a"
MIDDLE_EDGE = "#b8355c"
INNER = "#f57a9c"
INNER_EDGE = "#d95a80"
HIGHLIGHT = "#ffb0c4"
HIGHLIGHT_EDGE = "#ef8ba6"

GOLD = "#f5c84c"
GOLD_DOT = "#8a5a20"

Y = -30  # base of the flower / top of the stem


# =========================================================
# POLYGON / ELLIPSE HELPERS
# =========================================================

def polygon(points, fill, outline=None, width=1.5):
    t.width(width)
    t.fillcolor(fill)
    t.pencolor(outline if outline else fill)
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()
    t.penup()


def ellipse(cx, cy, rx, ry, color, outline=None):
    points = []
    for i in range(73):
        a = 2 * math.pi * i / 72
        points.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    polygon(points, color, outline)


# =========================================================
# WATER
# =========================================================

def draw_water():
    t.fillcolor(WATER)
    t.pencolor(WATER)
    t.goto(-1000, -270)
    t.pendown()
    t.begin_fill()
    t.goto(1000, -270)
    t.goto(1000, -700)
    t.goto(-1000, -700)
    t.goto(-1000, -270)
    t.end_fill()
    t.penup()

    t.pencolor(WATER_LINE)
    for y, width in [(-300, 300), (-335, 460), (-370, 630), (-405, 800)]:
        t.width(2)
        t.goto(-width / 2, y)
        t.pendown()
        t.forward(width)
        t.penup()


# =========================================================
# STEM - a single smooth S-curve instead of a jagged zigzag
# =========================================================

def _stem_curve(x_amp, y0, y1, steps=40):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        y = y0 + (y1 - y0) * u
        x = x_amp * math.sin(math.pi * 1.4 * u)
        pts.append((x, y))
    return pts


def draw_stem():
    t.pencolor(STEM)
    t.width(11)
    pts = _stem_curve(6, -280, Y)
    t.goto(pts[0])
    t.pendown()
    for p in pts[1:]:
        t.goto(p)
    t.penup()

    t.pencolor(STEM_LIGHT)
    t.width(3)
    pts = _stem_curve(6, -272, Y)
    t.goto(pts[0][0] + 2, pts[0][1])
    t.pendown()
    for p in pts[1:]:
        t.goto(p[0] + 2, p[1])
    t.penup()


# =========================================================
# LILY PAD (leaf) - a round pad with a notch, not a pointy oval
# =========================================================

def draw_leaf(cx, cy, radius, angle_deg, notch_deg=28):
    points = []
    steps = 80
    start = notch_deg / 2
    end = 360 - notch_deg / 2
    for i in range(steps + 1):
        a = start + (end - start) * i / steps
        rad = math.radians(a)
        r = radius * (1 + 0.03 * math.sin(4 * rad))  # gentle organic wobble
        x = r * math.cos(rad)
        y = r * math.sin(rad) * 0.55  # squashed for a front-on perspective
        rot = math.radians(angle_deg)
        rx = x * math.cos(rot) - y * math.sin(rot)
        ry = x * math.sin(rot) + y * math.cos(rot)
        points.append((cx + rx, cy + ry))
    points.append((cx, cy))
    polygon(points, LEAF, LEAF_LIGHT, width=2)

    t.pencolor(LEAF_LIGHT)
    t.width(1.5)
    rot = math.radians(angle_deg)
    for a in range(int(start) + 15, int(end), 35):
        rad = math.radians(a)
        r = radius * 0.92
        x = r * math.cos(rad)
        y = r * math.sin(rad) * 0.55
        rx = x * math.cos(rot) - y * math.sin(rot)
        ry = x * math.sin(rot) + y * math.cos(rot)
        t.goto(cx, cy)
        t.pendown()
        t.goto(cx + rx, cy + ry)
        t.penup()


# =========================================================
# PETAL - a symmetric teardrop: rounded base, pointed tip.
# This replaces the old sin(a)*sin(a/2) shape, which produced
# lopsided, twisted blades instead of real petals.
# =========================================================

def petal_points(length, width, tip_pinch=0.55):
    pts = []
    steps = 36
    for i in range(steps + 1):
        u = i / steps
        x = length * u
        env = math.sin(math.pi * u) ** tip_pinch
        pts.append((x, width * env))
    for i in range(steps, -1, -1):
        u = i / steps
        x = length * u
        env = math.sin(math.pi * u) ** tip_pinch
        pts.append((x, -width * env))
    return pts


def draw_petal(cx, cy, angle_deg, length, width, color, edge, curl=0.0):
    rad = math.radians(angle_deg)
    raw = petal_points(length, width)
    pts = []
    for (x, y) in raw:
        bend = curl * (x / length) ** 2 if length else 0
        rx = x * math.cos(rad) - (y + bend) * math.sin(rad)
        ry = x * math.sin(rad) + (y + bend) * math.cos(rad)
        pts.append((cx + rx, cy + ry))
    polygon(pts, color, edge, width=1.5)

    t.pencolor(edge)
    t.width(1)
    t.goto(cx, cy)
    t.pendown()
    t.goto(cx + length * 0.92 * math.cos(rad), cy + length * 0.92 * math.sin(rad))
    t.penup()


# =========================================================
# FULL LOTUS BLOOM - four overlapping layers, small to large,
# fanned upward like a real open lotus, plus a seed-pod center.
# =========================================================

def draw_lotus():
    cx, cy = 0, Y + 10

    back_angles = [15, 40, 65, 90, 115, 140, 165]
    for a in back_angles:
        draw_petal(cx, cy, a, 175, 46, OUTER, OUTER_EDGE, curl=8)
        screen.update()
        time.sleep(0.06)

    mid_angles = [27, 52, 77, 102, 127, 152]
    for a in mid_angles:
        draw_petal(cx, cy, a, 150, 40, MIDDLE, MIDDLE_EDGE, curl=6)
        screen.update()
        time.sleep(0.07)

    inner_angles = [40, 65, 90, 115, 140]
    for a in inner_angles:
        draw_petal(cx, cy, a, 118, 30, INNER, INNER_EDGE, curl=3)
        screen.update()
        time.sleep(0.08)

    hi_angles = [55, 78, 102, 125]
    for a in hi_angles:
        draw_petal(cx, cy, a, 68, 17, HIGHLIGHT, HIGHLIGHT_EDGE, curl=2)
        screen.update()
        time.sleep(0.09)

    ellipse(cx, cy + 58, 22, 15, GOLD, "#c99a2e")
    for a in range(0, 360, 40):
        r = 12
        px = cx + r * math.cos(math.radians(a))
        py = cy + 58 + r * math.sin(math.radians(a)) * 0.8
        ellipse(px, py, 2.2, 2.2, GOLD_DOT)
    screen.update()


# =========================================================
# ANIMATION
# =========================================================

draw_water()
screen.update()
time.sleep(0.4)

draw_stem()
screen.update()
time.sleep(0.4)

draw_leaf(-230, -245, 105, 200)
screen.update()
time.sleep(0.2)

draw_leaf(190, -260, 90, 15)
screen.update()
time.sleep(0.4)

draw_lotus()

t.pencolor("#168dd1")
t.goto(0, -450)
t.write("LOTUS", align="center", font=("Arial", 22, "bold"))
screen.update()

# =========================================================
# RUN
# =========================================================

screen.tracer(1, 10)
screen.mainloop()