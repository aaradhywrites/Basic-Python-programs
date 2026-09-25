import turtle as t, math as m, time

s = t.Screen(); s.setup(700, 700)
s.bgcolor("black"); s.tracer(0)

# --- Fullscreen launch ---
root = s.getcanvas().winfo_toplevel()
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))  # Esc to exit fullscreen
root.bind("<q>", lambda e: s.bye())  # q to quit

p = t.Turtle(); p.hideturtle()
C = ["#ff0055", "#ff5500", "#ffcc00", "#33ff00", "#00ffcc", "#0066ff", "#9900ff", "#ff00cc"]

# Shuriken outline: 4 outer spikes + 4 inner notches (8 vertices)
outer_r = 250
inner_r = 70
n_points = 4
V = []
for k in range(n_points):
    a_out = m.pi / 2 + k * (2 * m.pi / n_points)
    a_in = a_out + (m.pi / n_points)
    V.append((outer_r * m.cos(a_out), outer_r * m.sin(a_out)))
    V.append((inner_r * m.cos(a_in), inner_r * m.sin(a_in)))
V.append(V[0])

targets = [
    (V[i][0] + (j / 10) * (V[i + 1][0] - V[i][0]),
     V[i][1] + (j / 10) * (V[i + 1][1] - V[i][1]))
    for i in range(len(V) - 1) for j in range(10)
]
for i, (tx, ty) in enumerate(targets):
    col = C[i % len(C)]
    p.pencolor(col); p.width(1)
    p.penup(); p.goto(0, 0); p.pendown()
    p.goto(tx, ty)

    p.pencolor("#ffffff" if i % 2 == 0 else col); p.width(1)
    for r in (0, m.pi / 4, m.pi / 2, 3 * m.pi / 4):
        dx, dy = 5 * m.cos(r), 5 * m.sin(r)
        p.penup(); p.goto(tx - dx, ty - dy); p.pendown(); p.goto(tx + dx, ty + dy)

    s.update(); time.sleep(0.02)

s.update(); t.done()