from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import urllib.request
import pickle


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
