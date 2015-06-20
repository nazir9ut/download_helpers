import pprint
pp = pprint.PrettyPrinter(indent=4)
def mprint(str):
    pp.pprint(str)

from olx_helpers import *



for page_num in range(500):

    urls = get_urls(2)

    for url in urls:
        print(url)
        download_photos_by_page_url(url)




download_photos_by_page_url('http://alma-ata.alm.olx.kz/obyavlenie/prodam-toyota-haylander-toyota-highlander-2008-ID5sYUN.html#adf81a6553;promoted')