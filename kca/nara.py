# made by leety
# 2020-04
# openpyxl? pandas? 뭐 쓸 지 고민 중
# pip install bs4 openpyxl
# pip install pyinstaller // 실행 파일로 만들기 위한 패키지
from datetime import timedelta, date
from bs4 import BeautifulSoup
import multiprocessing
import requests
import pandas
import sys

sys.stdout = open('c:\\python\\test4.txt', 'w', encoding='UTF-8')

global q
q = multiprocessing.Queue()

def crawling(index):
    # 오늘 날짜와 30일(약 1달) 전 날짜 구하기
    today = str(date.today()).replace('-', '/')
    today_30d = str(date.today()+timedelta(days=-30)).replace('-', '/')

    lists_list = []

    try:
        url = "http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=5&searchDtType=1&fromBidDt=%s&toBidDt=%s&radOrgan=1&regYn=Y&bidSearchType=1&searchType=1&currentPageNo=%d" %(today_30d, today, index)
        webpage = requests.get(url).text
        html = BeautifulSoup(webpage, "html.parser")

        find_tr = html.find('tbody')

        trs = find_tr.findAll('tr')
        for tr in trs:
            lists = []
            divs = tr.findAll('div')

            for div in divs:
                lists.append(div.text)
            lists_list.append(lists)

        return lists_list

    except:
        return

def print_crawling(index):
    global q
    q.put(crawling(index))

if __name__ == "__main__":
    Pool = multiprocessing.Pool(processes=4)
    Pool.map(print_crawling, range(1, 50))

    print(q.get())
    q.close()