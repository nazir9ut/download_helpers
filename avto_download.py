
import socket
socket.setdefaulttimeout(60)

from avto_helpers import *





total_pages = 20080

# todo
current_page = 1180

def download(start_page, total_pages):

    for page_num in xrange(start_page, total_pages, 1):
        print("PAGE NUMBER = " + str(page_num))

        # todo
        global current_page
        current_page = page_num


        # get all page_ids from this page
        page_ids = get_page_ids(page_num)


        download_photos_by_page_ids(page_ids)



while True:
    try:
        download(start_page = current_page, total_pages = total_pages)
    except IOError:
        print("-------------------------------------------------------------------------------------------------------Naz, Time out")
    else:
        break






