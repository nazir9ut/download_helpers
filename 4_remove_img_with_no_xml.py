import glob
import os
import ntpath
import shutil

from PIL import Image


for name in glob.glob('/home/naz/Desktop/avto_6500/all_img/*'):

    all_xml_path = '/home/naz/Desktop/avto_6500/all_xml'

    file_name = ntpath.basename(name)

    file_name_no_ext = file_name.split('.')[0]

    xml_file = all_xml_path + '/' + file_name_no_ext + '.xml'


    if not os.path.isfile(xml_file):
        print name + '---'
        # os.remove(name)
