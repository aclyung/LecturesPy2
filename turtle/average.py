a = ["국어", "영어", "수학"]
grade = [int(input(v + "점수: ")) for v in a]
sum = 0
for v in grade:
    sum += v

print(sum / len(grade))
