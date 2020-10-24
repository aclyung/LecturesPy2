import turtle, time

l = [int(input("길이")) for i in range(2)]

turtle.shape("turtle")
for i in range(5):
    turtle.circle(l[0])
    turtle.forward(l[1])

time.sleep(5)
turtle.reset()
turtle.done()