import numpy as np
import cv2
from db import *
import json


all_rows = Avtonomera.select()


scaled_img_path = '/home/naz/Desktop/avto_6500/all_img_scaled'


for row in all_rows:

    rectangles = []

    objects = json.loads(row.scaled_points)

    for object in objects:
        points_arr = []

        for point in object:
            points_arr.append([point['x'], point['y']])


        rect = cv2.boundingRect(np.array(points_arr))
        rectangles.append(rect)
        # cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (255,0,0), 2)

    row.bounding_rects = json.dumps(rectangles)
    row.save()






