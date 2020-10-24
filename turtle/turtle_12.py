import turtle

distance = int(input("거리: "))
turtle.shape("turtle")
for i in range(3):
    turtle.forward(distance)
    turtle.right(90)

turtle.done()