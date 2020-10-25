import turtle as tt
import time

# length = int(input("길이: "))
# tt.shape("turtle")
# for i in range(5):
#     tt.forward(length * (2 ** i))
#     tt.right(45)
# time.sleep(3)

# length = int(input("길이: "))
# tt.shape("turtle")
# for i in range(5, 0, -1):
#     tt.forward(length * (2 ** i))
#     tt.right(45)

# time.sleep(3)

length = int(input("길이: "))
tt.shape("turtle")
# tt.left(180)
for i in range(5, 0, -1):
    tt.goto(0, 0)
    tt.forward(length * (2 ** i))
    tt.right(45)
