'http://www.cardatabase.net/search/search.php?nr_of_results=250277&page_limit=250277&view=thumbnails&first_this_page=130'



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


r = requests.get('http://www.cardatabase.net/search/search.php?nr_of_results=250277&page_limit=1000&view=thumbnails&first_this_page=130')

print(r.text)