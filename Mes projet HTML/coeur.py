import random
import math
import turtle

ecran = turtle.Screen()
ecran.bgcolor("black")
ecran.title("Un cœur pour toi")
ecran.setup(width=900, height=700)
ecran.tracer(0)

stylo = turtle.Turtle()
stylo.hideturtle()
stylo.penup()

for _ in range(1800):
    t = random.uniform(0, 2 * math.pi)

    x = 16 * math.sin(t) ** 3
    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

    stylo.goto(x * 20, y * 20)
    stylo.color(random.choice(["hot pink", "pink", "deep pink"]))
    stylo.write("LOVE YOU", align="center", font=("Arial", 8, "bold"))

ecran.update()
turtle.done()