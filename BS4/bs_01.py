import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

day = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def open_link():
    html = [urlopen(
        "https://comic.naver.com/webtoon/weekdayList.nhn?week=" + v) for v in day]
    return [BeautifulSoup(htm, "html.parser", from_encoding='utf-8')
            for htm in html]


def scrap():
    soup = open_link()
    container = [sup.find('div', class_='view_type')for sup in soup]
    week = [con.find('h3', class_="sub_tit").text for con in container]
    tag_dt_list = [sup.find('ul', class_='img_list').find_all('dt')
                   for sup in soup]
    titles_list = []
    for tag_dt in tag_dt_list:
        titles = []
        for tag_a in tag_dt:
            dictn = {}
            dictn['title'] = tag_a.find('a').attrs['title']
            dictn['url'] = tag_a.find('a').attrs['href']
            titles.append(dictn)
        titles_list.append(titles)

    webtoon = []
    for w, t in zip(week, titles_list):
        wek = {}
        wek["week"] = w
        wek['titles'] = t
        webtoon.append(wek)

    return webtoon


def save():
    with open("webtoon_list.json", "w", encoding='UTF-8') as jsonfile:
        json.dump(scrap(), jsonfile, ensure_ascii=False)


save()
