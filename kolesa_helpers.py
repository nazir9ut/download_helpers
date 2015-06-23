import requests
import urllib
from bs4 import BeautifulSoup
import os.path
from os import listdir
from os.path import isfile, join
import numpy as np




def download_photos_by_page_id(page_id, path = '/media/naz/3534-E743/kolesa_downloads'):
    r = requests.get('http://kolesa.kz/a/show/' + page_id)

    soup = BeautifulSoup(r.text)

    photos_a = soup.find_all("a", class_="photo")
    for p in photos_a:
        path_and_file = path + "/" + page_id + "_" + p['href'].rsplit('/',1)[1]

        exists = os.path.isfile(path_and_file)
        if not exists:
            # print(p['href'])
            print(p['href'].rsplit('/',1)[1])
            urllib.urlretrieve (p['href'], path_and_file)
        else:
            print("EXISTS")
            print(p['href'])

        print("-------------------------------------------------")







def download_photos_by_page_ids(page_ids):
    for page_id in page_ids:
        download_photos_by_page_id(page_id)










def remove_downloaded_page_ids(page_ids, path = '/media/naz/3534-E743/kolesa_downloads'):

    result = []

    files = [ f for f in listdir(path) if isfile(join(path,f)) ]


    for page_id in page_ids:
        # find if there's any file from this page id in download folder
        tmp = [page_id for s in files if page_id in s]

        # if there downloaded files from this page_id, then skip it
        if len(tmp) > 0 :
            continue
        else:
            result.append(page_id)


    return  result






# page num
# 4733
#
# return all page_ids from page like this
# http://kolesa.kz/cars/?page=4733
def get_page_ids(page_num):

    result = []

    params = {'page': page_num}

    r = requests.get('http://kolesa.kz/cars/', params = params)


    soup = BeautifulSoup(r.text)

    pages_a = soup.find_all("a", class_="mm")

    for a in pages_a:
        page_id = a['href'].rsplit('/',1)[1]
        result.append(page_id)


    return result














def get_total_pages():
    r = requests.get('http://kolesa.kz/cars/')

    soup = BeautifulSoup(r.text)

    result = soup.find("td", class_="buttons").find_all('a')[-1].text

    result = int(result)

    return result