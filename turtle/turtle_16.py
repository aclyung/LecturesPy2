import random
import turtle as tt

tt.shape("turtle")
while True:
    tt.penup()
    tt.goto(random.randint(-300, 300), random.randint(-300, 300))
    tt.pendown()
    tt.circle(random.randrange(100))