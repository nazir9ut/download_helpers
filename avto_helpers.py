import requests
import urllib
from bs4 import BeautifulSoup
import os.path
from os import listdir
from os.path import isfile, join
import numpy as np

import urllib.request


import pprint
pp = pprint.PrettyPrinter(indent=4)
def mprint(str):
    pp.pprint(str)





def get_page_ids(page_num):

    result = []

    print('page_num ' + str(page_num))

    r = requests.get('http://platesmania.com/ee/gallery-' + str(page_num))




    soup = BeautifulSoup(r.text, "lxml")

    foto_hold_div = soup.find('div', class_="col-md-9")


    # print foto_hold_div


    # nomer_links = foto_hold_div.select('a[href~="nomer"]')
    # nomer_links = foto_hold_div.find_all("a", {"href" : "/kz/nomer8736638"})
    nomer_links = foto_hold_div.select('a[href*=nomer]')



    # print(nomer_links)



    page_ids = [link['href'].split("nomer",1)[1] for link in nomer_links]





    page_ids = list(set(page_ids))


    return page_ids






def download_photos_by_page_id(page_id, path = '/home/naz/Desktop/ee'):

    exists = os.path.isfile(path + "/" + page_id + '.jpg')

    if not exists:
        r = requests.get('http://platesmania.com/ee/foto' + page_id)

        soup = BeautifulSoup(r.text, "lxml")

        img_tag = soup.find("img")



        if img_tag:
            src = img_tag['src']

            if src:
                path_and_file = path + "/" + src.rsplit('/', 1)[1]


                print('DOWNLOADING ...' + src)
                print('TO DIR ...' + path_and_file)


                req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
                html = urllib.request.urlopen(req).read()

                with open(path_and_file, 'wb') as file_:
                    file_.write(html)


    else:
        print("EXISTS")










def download_photos_by_page_ids(page_ids):
    for page_id in page_ids:
        download_photos_by_page_id(page_id)