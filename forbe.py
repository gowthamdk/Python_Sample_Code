#from splinter import Browser
import time
import urllib2
import requests
from bs4 import BeautifulSoup
import sys


url = "http://data.worldbank.org/country/"
request = requests.get(url)
home_page = request.text
bs = BeautifulSoup(home_page,'html.parser')
name = bs.find_all("div", "views-field-name")
all_link = [div.a["href"] for div in name]
#print all_link
#sys.exit()
for link in all_link:
    page = requests.get(link)
    page = page.text
    bs = BeautifulSoup(page,'html.parser')
    data = bs.find("li", {"class": "download-xls first"})
    excel = data.find('a')["href"]
    print excel
    fname = excel.split('/')[-1].split('?')[0]
    print fname
    r = requests.get(excel)
    f = open('downloads/'+fname+'.xls', 'wb')
    #print r.content
    f.write(r.content)
    f.close()
    #for tr in bs.find_all('tr', {'class', 'name'}):
        #link = tr['href']

##    for i in range(2000):
##        browser.find_by_xpath("//span[contains(@class, 'next-number')]").click()
##        time.sleep(5)
##        print str(i)
