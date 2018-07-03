from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import urllib.request

js = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(js)
driver.set_window_size(1400,1000)
driver.get('https://www.alignable.com/timonium-md/directory')
time.sleep(6)

close = driver.find_elements_by_xpath('//*[@id="shared-modal"]/div/div[3]/div[2]/a')
close[0].click()

x=1000
while x < 225000:
    driver.execute_script("window.scrollTo(0, " + str(x) + ")")
    time.sleep(0.09)
    x = x + 1000

html = driver.page_source

soup = BeautifulSoup(html, 'lxml')
data = soup.findAll('div',attrs={'class':'business-attribution__business-info'})
for div in data:
    links = div.findAll('a')
    for a in links:
        print(a['href'])

for a in links:
    f = urllib.request.urlopen(str(a['href']))
    soupy = BeautifulSoup(f, 'lxml')
    datay = soupy.findAll('div',attrs={'class':'u--td profile-info__item'})
    for divy in datay:
        linky = divy.findAll('a')
        for lunk in linky:
            print(a['href'])
