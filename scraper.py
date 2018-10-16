from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import urllib.request
from urllib.parse import urlparse
import pickle
import os

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

hunks = []
newLunks = []

soup = BeautifulSoup(open("C:\\somthing.html", encoding="utf8"), "html.parser")
data = soup.findAll('div',attrs={'class':'business-attribution__business-info'})
for div in data:
    blinks = div.findAll('a')
    for a in blinks:
        hunks.append(a['href'])
countdown = len(hunks)

for link in hunks:
    try:
        print(countdown)
        request = urllib.request.urlopen(link)
        soupy = BeautifulSoup(request, 'lxml')
        datay = soupy.findAll('div',attrs={'class':'u--td profile-info__item'})
        for divy in datay:
            linky = divy.findAll('a')
            for a in linky:
                newLunks.append(a['href'])
        countdown = countdown - 1
    except:
        countdown = countdown - 1
        pass

with open('testfile2.txt', 'wb') as fp:
    pickle.dump(newLunks, fp)

with open ('testfile2.txt', 'rb') as fp:
    itemlist = pickle.load(fp)
newlist = []
for item in itemlist:
    if "tel:" in item:
        pass
    elif "face" in item:
        pass
    else:
        newlist.append(item)

with open('testfile3.txt', 'wb') as fp:
    pickle.dump(newlist, fp)

with open ('testfile3.txt', 'rb') as fp:
    weblist = pickle.load(fp)

for website in weblist:
    parsed_url = urlparse(website)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
    webaddr = '{uri.netloc}'.format(uri=parsed_url)
    print(domain)
    print(webaddr)
    #os.system(r"C:\wget.exe --recursive --no-clobber --convert-links --adjust-extension --domains " + domain + " " + website)
