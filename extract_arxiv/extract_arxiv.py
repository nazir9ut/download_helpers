from bs4 import BeautifulSoup
import re
import os


import urllib

from db import *




path_and_file = '/home/naz/Desktop/Deep Learning.html'


uid = os.path.basename(path_and_file)


soup = BeautifulSoup(open(path_and_file), "lxml")


body = soup.body


# src = 'http://arxiv.org/pdf/1311.2524v2.pdf'
#
#
# urllib.urlretrieve (src, "/home/naz/Desktop/1311.2524v2.pdf")




all = []

count = 0
for elem in body.find_all('a', text=re.compile(r'^http\:\/\/arxiv.org')):

    text = elem.text

    if text not in all:
        all.append(text)
        print text
    else:
        print 'exist'
        print text



    query = Arxiv.select().where(Arxiv.name == text)

    if not query.exists():
        Arxiv.create(name = text)
