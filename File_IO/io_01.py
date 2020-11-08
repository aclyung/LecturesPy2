import os
filedir = os.path.dirname(os.path.abspath(__file__))
with open("./tmp/data_01.txt", "r", encoding="UTF-8") as txt:
    list = txt.read().splitlines()

for i in range(len(list)):
    print(str(i+1) + " "+list[i])
# with open("./BS4/webtoon_list.json", "r", encoding="UTF-8") as txt_file:
#     inlist = txt_file.read().splitlines()
#     print(inlist)
