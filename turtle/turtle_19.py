import turtle as tt


radius = int(input("radius: "))
print("Radius size:", radius)
outer = int(input("outer (0 or 1):")) == 1
print("Drawing Outer" if outer else "Not Drawing Outer")
stype = int(input("stype (integer 3-5):"))
shape = stype >= 3 and stype <= 5
print("Drawing Steps" if shape else "Not Drawing Steps")

tt.shape("turtle")
if outer:
    tt.circle(radius)
    if shape:
        tt.circle(radius, steps=stype)
    tt.done()
elif shape:
    tt.circle(radius, steps=stype)
    tt.done()
else:
    pass
