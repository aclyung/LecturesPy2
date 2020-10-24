import turtle as tt

tt.shape("classic")
tt.right(90)
tt.forward(200)
for i in range(2):
    tt.penup()
    tt.goto(-(i + 1) * 30, 0)
    tt.down()
    tt.forward(200)

tt.done()