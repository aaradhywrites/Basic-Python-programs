import turtle as tu

t, s = tu.Turtle(), tu.Screen()
s.setup(1.0, 1.0) 
s.bgcolor("black")
t.speed(0)
t.pencolor("cyan")

for i in range(120):
    t.lt(8); t.fd(100); t.rt(175)
    for _ in range(4):
        t.fd(i); t.lt(6)

s.exitonclick()