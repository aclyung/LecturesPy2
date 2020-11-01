import turtle as tt

shape = input("모양: ")
if shape == "삼각형":
    length = int(input("변 길이:"))
    tt.shape("turtle")
    for i in range(3):
        tt.forward(length)
        tt.left(120)
    tt.done()
elif shape == "사각형":
    l = ["가로", "세로"]
    lengths = [int(input(v + ": ")) for v in l]
    for i in range(4):
        tt.shape("turtle")
        tt.forward(lengths[i % 2])
        tt.left(90)
    tt.done()
else:
    pass
