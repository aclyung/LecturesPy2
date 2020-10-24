import turtle
import random
import time

turtle.penup()
turtle.shape("turtle")
for i in range(30):
    random.seed(time.time())
    loc = [random.randrange(200) for i in range(2)]
    turtle.goto(loc[0], loc[1])

    turtle.stamp()
    time.sleep(1)

turtle.done()