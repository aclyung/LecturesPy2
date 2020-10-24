import turtle

length = int(input("길이: "))
turtle.shape("turtle")
for i in range(3):
    turtle.forward(length)
    turtle.left(120)
turtle.done()