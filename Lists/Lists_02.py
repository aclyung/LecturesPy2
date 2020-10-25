list_m = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
list_c = [[v + 5 for v in i] for i in list_m]
print(list_c)

list_n = []

for l in list_c:
    ll = []
    for i in l:
        ll.append(i + 5)
    list_n.append(ll)

print(list_n)

for i in range(1, 10):
    for v in range(2, 10):
        print("%d X %d = %2d" % (v, i, (v * i)), end=" | ")
    print("")
