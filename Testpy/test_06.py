sec = int(input("초: "))
min = sec // 60
sec = sec % 60
print("{}분 {}초".format(min, sec))
