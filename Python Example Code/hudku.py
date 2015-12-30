from splinter import Browser
from bs4 import BeautifulSoup
import sys
import time
import json
with Browser() as browser:
    file_handler = open("Huduku_Bakery_Ambatt.xls","w")
    browser.visit("http://www.hudku.com/search?q=Bakery+in++Ambattur%2C+Chennai%2C+Tamil+Nadu%2C+India&l=true")
    time.sleep(5)
    page_read = str((browser.html).encode('UTF-8'))
    bs = BeautifulSoup(page_read)
    pages = bs.find("ul",{"id":"idPaginationList"})
    li = pages.find_all("li")
    count = int(li[len(li)-2].text.strip())
    print count
    sys.exit()
    i = 1
    while i<=count :
        print i
        geo =  bs.find("input",{"name":"responseJson"})
        json_str =  geo['value']
        data = json.loads(json_str)
        page_read = str((browser.html).encode('UTF-8'))
        bs = BeautifulSoup(page_read)
        json_count = 0
        for div in bs.find_all("div",{"class":"listing_box"}):
            name_tag = div.find("span",{"class":"name"})
            name = name_tag.text.strip()
            addr_tag = div.find("p",{"class":"address"})
            addr = (' ').join(addr_tag.text.strip().split('\n'))
            contact_tag = div.find("div",{"class":"contact_left"})
            contact = contact_tag.text.strip()
            print name
            content = (div.text).split('\n')
            final_content = filter(None, content)
            final_content = ('\t').join(final_content)
            try :
                Lat = data['listings'][json_count]['listingLatitude']
                Long = data['listings'][json_count]['listingLongitude']
            except :
                Lat = "N/A"
                Long = "N/A"                
            file_handler.write(name.encode("UTF-8")+"\t"+addr.encode("UTF-8")+"\t"+contact.encode("UTF-8")+"\t"+Lat.encode("UTF-8")+"\t"+Long.encode("UTF-8")+"\n")
            json_count += 1
        if i!=count:
            next_button = browser.find_by_xpath("//button[contains(@class, 'next')]")
            next_button.click()
            time.sleep(5)
        i = i+1
file_handler.close()
