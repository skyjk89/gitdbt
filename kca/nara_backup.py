# made by leety
# 2020-04
# openpyxl? pandas? 뭐 쓸 지 고민 중
# pip install bs4 openpyxl
# pip install pyinstaller // 실행 파일로 만들기 위한 패키지
from datetime import timedelta, date
from bs4 import BeautifulSoup
import requests
import pandas
import sys

sys.stdout = open('c:\\python\\test2.txt', 'w', encoding='utf8')

"""
# 엑셀 파일로 내보내기...!
write_wb = Workbook()
write_ws = write_wb.active
"""

# 오늘 날짜와 30일(약 1달) 전 날짜 구하기
today = str(date.today()).replace('-', '/')
today_30d = str(date.today()+timedelta(days=-30)).replace('-', '/')

lists_list = []
lists = []
for index in range(1, 100):
    try:
        url = "http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=5&searchDtType=1&fromBidDt=%s&toBidDt=%s&radOrgan=1&regYn=Y&bidSearchType=1&searchType=1&currentPageNo=%d" %(today_30d, today, index)
        webpage = requests.get(url).text
        html = BeautifulSoup(webpage, "html.parser")

        find_div = html.find('table')

        divs = find_div.findAll('div')
        for div in divs:
            lists.append(div.text)
        lists_list.append(lists)
    except:
        break

print(lists_list)