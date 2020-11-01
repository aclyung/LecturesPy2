score = [80, 70, 0]
grades = ["잘함", "보통", "미흡"]
cla = ["국어", "영어", "수학"]
u_scores = [
    [int(input(str(v) + "번 학생 " + str(cla[i]) + ": ")) for i in range(len(cla))]
    for v in range(1, 3)
]
averages = []
for i in u_scores:
    total = 0
    for v in i:
        total += v
    total = total / len(cla)
    averages.append(total)

for i in averages:
    for v in score:
        if i >= v:
            print(str(i), "번 학생 성적", grades[score.index(v)])
            break
        else:
            pass
