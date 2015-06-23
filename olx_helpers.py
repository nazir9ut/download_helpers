import requests
import urllib
from bs4 import BeautifulSoup
import os.path







def download_photos_by_page_url(url, path = '/media/naz/3534-E743/olx_downloads'):
    r = requests.get(url)

    print("url")
    print(url)

    soup = BeautifulSoup(r.text)

    photos_a  = soup.find('ul', id='bigGallery').find_all('a')


    for p in photos_a:

        if p['href']:
            path_and_file = path + '/' + p['href'].rsplit('/',1)[1]

            exists = os.path.isfile(path_and_file)

            if not exists:
                urllib.urlretrieve (p['href'], path_and_file)
                print(p['href'].rsplit('/',1)[1])
            else:
                print("EXISTS")









def get_urls(page_num):

    result = []

    params = {'page': page_num}

    r = requests.get('http://olx.kz/transport/legkovye-avtomobili/', params = params)


    soup = BeautifulSoup(r.text)

    pages_a = soup.select("a.marginright5.detailsLink")


    for a in pages_a:
        url = a['href']
        result.append(url)



    return result





