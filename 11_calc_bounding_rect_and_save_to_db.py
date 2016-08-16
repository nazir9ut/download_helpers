import numpy as np
import cv2
from db import *
import json
import PIL
from PIL import Image


all_rows = Avtonomera.select()


scaled_img_path = '/home/naz/Desktop/avto_6500/all_img_scaled'



for row in all_rows:

    rectangles = []

    objects = json.loads(row.scaled_points)

    img = Image.open(scaled_img_path + '/' + row.name)

    img_width = img.size[0]
    img_height = img.size[1]


    for object in objects:
        points_arr = []

        for point in object:
            points_arr.append([point['x'], point['y']])


        rect = cv2.boundingRect(np.array(points_arr))


        xmin = rect[0]
        ymin = rect[1]
        xmax = rect[0] + rect[2]
        ymax = rect[1] + rect[3]


        if xmin == 0:
            xmin = 1


        if ymin == 0:
            ymin = 1


        if rect[2] <= 3:
            print 'rect[2] <= 3'
            print rect

        if rect[3] <= 3:
            print 'rect[3] <= 3'
            print rect


        if xmax >= img_width:
            print 'xmax > img_width'
            print xmax
            xmax = img_width - 1
            # pass

        if ymax >= img_height:
            print 'ymax > img_height'
            print ymax
            ymax = img_height




        rectangles.append([xmin, ymin, xmax, ymax])


    row.bounding_rects = json.dumps(rectangles)
    row.save()






