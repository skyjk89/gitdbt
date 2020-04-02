# import sys
from bs4 import BeautifulSoup
import requests

# sys.stdout = open("htmltest2.html", 'w', encoding="utf8")

search_word = "서울"
search_url = "https://kr.indeed.com/jobs?q=&l=서울"
search_url2 = "/jobs?q=&l={}".format(search_word)

webpage = requests.get(search_url).text
html = BeautifulSoup(webpage, "html.parser")
job_divs = html.findAll("div", {"class" : "jobsearch-SerpJobCard"}, limit=3)

for job_div in job_divs:
    try:
        print("=======================================================")
        print("업무명 : " + job_div.find('a', {'class':'jobtitle'}).text.strip())
        print("회사명 : " + job_div.find('span', {'class':'company'}).text.strip())
        print("지역명 : " + job_div.find('div', {'class':'location'}).text.strip())
        print("지급액 : " + job_div.find('span', {'class':'salaryText'}).text.strip())
    except:
        pass

print("=======================================================")