import turtle as tt
import time

length = int(input("길이: "))
tt.shape("turtle")
for i in range(5):
    tt.forward(length * (2 ** i))
    tt.right(45)
time.sleep(3)