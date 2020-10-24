import turtle

length = int(input("지름: "))

turtle.shape("turtle")
turtle.circle(length)
turtle.circle(length, steps=4)
turtle.done()
