##from splinter import Browser
##from time import sleep
##browser = Browser()
##url = "http://rural.nic.in/sites/bpl-census-2011.asp"
##browser.visit(url)
##sleep(5)
##browser.driver.save_screenshot('sreenshot.png')
##browser.quit()

from splinter import Browser
import time
browser = Browser()
browser.visit("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(browser.find_by_id("content").text)
browser.quit()
