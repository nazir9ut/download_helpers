import xml.etree.cElementTree as ET
import numpy as np
import cv2
from db import *
import json
import PIL
from PIL import Image


all_rows = Avtonomera.select()


scaled_img_path = '/home/naz/Desktop/avto_6500/all_img_scaled'


for row in all_rows:

    bounding_rects = json.loads(row.bounding_rects)

    for bounding_rect in bounding_rects:
        if bounding_rect[2] <= 3:
            # print bounding_rect
            pass
        if bounding_rect[3] <= 3:
            pass
            # print bounding_rect











    img = Image.open(scaled_img_path + '/' + row.name)

    # print img.size
    if img.size[0] != 500:
        if img.size[1] != 500:
            # print img.size
            pass


    for bounding_rect in bounding_rects:
        xmin = bounding_rect[0]
        ymin = bounding_rect[1]
        xmax = bounding_rect[0] + bounding_rect[2]
        ymax = bounding_rect[1] + bounding_rect[3]

        if xmax > 500:
            # print '> 500 x'
            # print xmax
            pass

        if ymax > 500:
            # print '> 500 y'
            # print ymax
            pass




