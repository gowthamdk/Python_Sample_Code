from splinter import Browser
from time import sleep

browser=Browser()
browser.visit("http://www.imd.gov.in/section/hydro/distrainfall/districtrain.html")
sleep(3)
links = [li.find_by_tag('a')['href'] for li in browser.find_by_tag('li')]

for link in links:
    browser.visit(link.strip())
    sleep(3)
    urls = [li.find_by_tag('a')['href'] for li in browser.find_by_tag('li')]
    #print urls
    for url in urls:
        browser.visit(url.strip())
        sleep(2)
        state = url.split("/")[-2]
        dist = url.split("/")[-1].replace(".txt","")
        print state+"|"+dist
        fh = open(state+"_"+dist+".xls", "w")
        data = browser.find_by_tag("pre")
        fh.write(data.text.strip().encode("UTF-8"))
        fh.close()



browser.quit()
