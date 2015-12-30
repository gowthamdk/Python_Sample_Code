from splinter import Browser
import sys
import time

def main(browser):
    fh = open("Gurudwaras_2.xls","w")
    fh.write("Name\tgeocode\n")
    for i in range(1,11):
        url = "http://www.holidayiq.com/New-Delhi-Gurudwaras-A-486-39-p"+str(i)+".html"
        browser.visit(url)
        time.sleep(3)
        links = [h5['href'] for h5 in browser.find_by_xpath('//h5/a[@title=""]')]
        for link in links:
            browser.visit(link)
            time.sleep(3)
            name = browser.find_by_xpath('//span[@itemprop="name"]')
            print name.text
            lat = browser.find_by_xpath('//meta[@itemprop="latitude"]')['content']
            lon = browser.find_by_xpath('//meta[@itemprop="longitude"]')['content']
            geocode = lat + "," + lon
            print geocode
            fh.write(name.text.strip().encode("UTF-8")+"\t" + str(geocode)+"\n")
    fh.close()

if __name__ == "__main__":
    browser=Browser()
    main(browser)
    browser.quit()


#xpath = '//p[@class="attrs"]/span[text()="description:"]



