import turtle as tt

# l = int(input("길이: "))
# d = int(input("간격: "))

# tt.shape("turtle")
# for i in range(3):
#     tt.goto(0, -d * i)
#     tt.down()
#     tt.forward(l + d * i)
#     tt.up()

# tt.done()
r = int(input("반지름: "))
tt.shape("turtle")
tt.circle(r)
tt.up()
tt.goto(0, r * 2)
tt.down()
tt.circle(r / 2)
tt.done()