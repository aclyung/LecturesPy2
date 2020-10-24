import turtle as tt

tt.shape("classic")
tt.forward(20)
for i in range(2):
    tt.left(90)
    tt.forward(50)
    tt.right(90)
    tt.forward((i + 1) * 10)
    tt.right(90)
    tt.forward(50)
    tt.left(90)
    tt.forward(20)
tt.done()
