import json
from urllib.request import urlopen
import urllib.request
import re
from bs4 import BeautifulSoup
import wget
with open("./webtoon_list.json", "r", encoding="UTF-8") as json_file:
    webobj = json.load(json_file)


def set_url(link):
    l = "https://comic.naver.com"+link
    print("Loading " + l)
    url = urlopen(l)
    return set_soup(url)


def set_soup(url):
    return BeautifulSoup(url, "html.parser", from_encoding='utf-8')


def get_title(sup):
    tds = sup.find('table').find_all('td', class_='title')
    titles = []
    for td in tds:
        titles.append(td.find('a'))
    return titles


status = 0
day = 0
soup = None
tile = ""
id = ""
while True:
    if status == 0:
        for til in webobj:
            print(til['week'])
        day = int(input("요일선택: "))
        if day <= len(webobj) and day > 0:
            status += 1
        if day == -1:
            print("Exit")
            break
        continue
    if status == 1:
        print()
        for tils, i in zip(webobj[day-1]['titles'], range(len(webobj[day-1]['titles']))):
            print(str(i+1)+": "+tils['title'], end=" | ")
        print()

        sel = int(input("타이틀 선택: "))
        if sel <= len(webobj[day-1]['titles']) and sel > 0:
            soup = set_url(webobj[day-1]['titles'][sel-1]['url'])
            tile = webobj[day-1]['titles'][sel-1]['title']
            status = 2

        elif sel == -1:
            status -= 1
        continue

    if status == 2:
        til = [a.text for a in get_title(soup)]
        link = [l.attrs['href'] for l in get_title(soup)]
        print()
        print(tile)
        for ti in range(len(til)):
            print(str(ti+1)+" "+til[ti], end=" | ")
        print()
        print("현재 페이지:" + soup.find('strong', class_='page').find('em').text)
        sel = int(input("타이틀 선택(-1은 뒤로, 0은 페이지 선택): "))

        if sel == -1:
            status -= 1
            continue

        if sel == 0:
            page = soup.find('div', class_='page_wrap').find_all(
                'a', class_='page')
            ps = []
            for p, k in zip(page, range(len(page))):
                ps.append(p.attrs['href'])
                print(str(k+1)+": "+p.text, end=" | ")

            while True:
                sell = int(input("페이지 선택(-1 to cancel): "))
                if sell <= len(ps) and sell > 0:
                    soup = set_url(ps[sell-1])
                    break
                elif sell == -1:
                    break
            continue
        elif sel <= len(til):
            soup = set_url(link[sel-1])
            id = til[sel-1]
            status += 1
            continue
    if status == 3:
        img_list = soup.find(
            'div', attrs={'id': 'comic_view_area'}).find_all('img', attrs={'alt': 'comic content'})
        imgs = [i.attrs['src'] for i in img_list]
        print(imgs)
        parse = re.sub('[-=.#/?:$}]', '', tile+" "+id)
        pp = re.sub(' +', '_', re.sub('[-=.#/?:$}]', '', id))

        fname = re.sub(' +', '_', parse)
        for lnk in range(len(imgs)):
            wget.download(imgs[lnk])
            # , out=tile+"/" +
            #               pp+"/"+fname+str(lnk)+'.jpg')

        print(fname)
        status = 0
