
import socket
socket.setdefaulttimeout(60)

from avto_helpers import *





total_pages = 1000

# todo
current_page = 0

def download(start_page, total_pages):

    for page_num in range(start_page, total_pages, 1):

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






