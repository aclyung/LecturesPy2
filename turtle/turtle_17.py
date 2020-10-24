import turtle as tt

t = int(input("주기: "))
p = int(input("크기: "))
tt.left(90)
for i in range(6):
    tt.forward(p)
    tt.right(90)
    tt.forward(t / 2)
    tt.right(90)
    tt.forward(p)
    tt.forward(p)
    tt.left(90)
    tt.forward(t / 2)
    tt.left(90)
    tt.forward(p)
