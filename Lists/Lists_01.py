list_m = [int(input("점수 {}: ".format(i))) for i in range(1, 4)]


def average(l):
    print(l)
    sum = 0
    for i in l:
        sum += i

    print("합: {}, 평균: {}".format(sum, sum / len(l)))


average(list_m)
nlist = [v + 5 for v in list_m]
average(nlist)
