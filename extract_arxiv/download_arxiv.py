import  urllib
import urllib2

from db import *
import helpers

import os


save_path = '/home/naz/Desktop/arxiv'


all_rows = Arxiv.select()

for row in all_rows:
    name = row.name

    if '.pdf' in name:
        # print name

        file_name = os.path.basename(name)

        # print file_name

        # urllib.urlretrieve (name, save_path + "/" + file_name)
    else:
        pdf_url = helpers.get_pdf_url_from_html(name)

        if pdf_url:
            file_name = os.path.basename(pdf_url)

            src = 'http://arxiv.org' + '/pdf/' +  file_name + '.pdf'

            file = save_path + "/" + file_name + '.pdf'

            print src
            print file

            urllib.urlretrieve (src, file)