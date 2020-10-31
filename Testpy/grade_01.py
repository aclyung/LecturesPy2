# score = [90, 80, 70, 60]
# grades = ["A", "B", "C", "D", "F"]
# u_score = int(input("성적입력: "))
# for i in score:
#     if u_score >= i:
#         print(grades[score.index(i)])
#         break
#     elif u_score < 60:
#         print(grades[4])
#         break
#     else:
#         continue
num = int(input("정수 입력: "))
if num > 0:
    print("양수")
elif num == 0:
    print(0)
else:
    print("음수")