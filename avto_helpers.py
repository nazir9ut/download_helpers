import requests
import urllib
from bs4 import BeautifulSoup
import os.path
from os import listdir
from os.path import isfile, join
import numpy as np

import pprint
pp = pprint.PrettyPrinter(indent=4)
def mprint(str):
    pp.pprint(str)





def get_page_ids(page_num):

    result = []

    r = requests.get('http://platesmania.com/kz/gallery.php?&type=2&start=' + str(page_num))


    soup = BeautifulSoup(r.text)

    foto_hold_div = soup.find('div', class_="foto-hold")

    nomer_links = foto_hold_div.select('a[href^="nomer"]')



    page_ids = [link['href'].split("nomer",1)[1] for link in nomer_links]

    page_ids = list(set(page_ids))


    return page_ids






def download_photos_by_page_id(page_id, path = '/media/naz/3534-E743/avto_nomera_downloads/kz/Private_owners_1993'):

    exists = os.path.isfile(path + "/" + 'kz' + page_id + '.jpg')

    if not exists:
        r = requests.get('http://platesmania.com/kz/foto' + page_id)

        soup = BeautifulSoup(r.text)

        img_tag = soup.find("img")


        src = img_tag['src']

        print('===================' + src)

        if src:
            path_and_file = path + "/" + src.rsplit('/', 1)[1]


            print('DOWNLOADING ...' + src)
            urllib.urlretrieve (src, path_and_file)
    else:
        print("EXISTS")



    print(path + "/" + 'kz' + page_id + '.jpg')
    print('------------------------------')









def download_photos_by_page_ids(page_ids):
    for page_id in page_ids:
        download_photos_by_page_id(page_id)