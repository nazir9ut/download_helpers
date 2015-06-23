import requests
import urllib
from bs4 import BeautifulSoup
import pprint
pp = pprint.PrettyPrinter(indent=4)
def mprint(str):
    pp.pprint(str)

from kolesa_helpers import *




total_pages =  get_total_pages()


for page_num in range(total_pages):
    print("PAGE NUMBER = " + str(page_num))

    page_ids = get_page_ids(page_num)

    print(len(page_ids))

    page_ids = remove_downloaded_page_ids(page_ids)

    print(len(page_ids))

    print('-------------------------')

    download_photos_by_page_ids(page_ids)




list = ['abc-123', 'def-456', 'ghi-789']
sub = 'abc'

print [s for s in list if sub not in s]






















# # search one tag inside the other




# mprint(soup.find_all("a", class_="photo"))




# download_photos('15877124')
# download_photos('23160434')



# # search only for one element (returns one element)
# mprint(soup.find('title'))



# # search by tag text
# mprint(soup.find_all("a", text="Lacie"))




# # search by attribute
# mprint(soup.find_all(attrs={"my_id": "444"}))



# # search for tags that match two or more CSS classes
# mprint(soup.select("a.myclass.sister"))



# print(soup.prettify())
# mprint(soup.find_all(class_="title"))



# def has_six_characters(css_class):
#     return css_class is not None and len(css_class) == 5
#
# mprint(soup.find_all(class_=has_six_characters))

