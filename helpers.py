import requests
import urllib
from bs4 import BeautifulSoup







def download_photos_by_page_id(page_id, path = 'downloads'):
    r = requests.get('http://kolesa.kz/a/show/' + page_id)

    soup = BeautifulSoup(r.text)

    photos_a = soup.find_all("a", class_="photo")
    for p in photos_a:
        print(p['href'])
        print(p['href'].rsplit('/',1)[1])
        urllib.urlretrieve (p['href'], path + "/" + page_id + "_" + p['href'].rsplit('/',1)[1])





def download_photos_by_page_ids(page_ids):
    for page_id in page_ids:
        download_photos_by_page_id(page_id)




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