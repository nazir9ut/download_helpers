from db import *

import glob
import os
import ntpath
import shutil

from PIL import Image


for name in glob.glob('/home/naz/Desktop/avto_6500/all_img/*'):

    # shutil.copy(name, '/home/naz/Desktop/avto_6500/all_xml')
    print name

    file_name = ntpath.basename(name)

    im=Image.open(name)

    width = im.size[0]
    height = im.size[1]




    query = Avtonomera.select().where(Avtonomera.name == file_name)

    if not query.exists():

        Avtonomera.create(name = file_name,
                          width = width,
                          height = height)


