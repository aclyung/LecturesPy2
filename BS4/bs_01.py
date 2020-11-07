
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen(
    "https://comic.naver.com/webtoon/weekdayList.nhn?week=sun")
soup = BeautifulSoup(html, "html.parser", from_encoding='utf-8')

container = soup.find('div', class_='view_type')
title = container.find('h3', class_="sub_tit")
names = container.find_all()
print(title.text)
