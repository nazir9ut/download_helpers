import requests
import urllib
from bs4 import BeautifulSoup
import os.path
from os import listdir
from os.path import isfile, join
import numpy as np



import pprint
import urllib2
import re




# html_url = 'http://arxiv.org/abs/1206.5538'
def get_pdf_url_from_html(html_url):

    page = urllib2.urlopen(html_url).read()

    soup = BeautifulSoup(page, "lxml")

    body = soup.body

    result = None

    for elem in body.find_all('a', text=re.compile(r'^PDF$')):
        # print elem['href']
        result = elem['href']

    return result



# print get_pdf_url_from_html('http://arxiv.org/abs/1206.5538')