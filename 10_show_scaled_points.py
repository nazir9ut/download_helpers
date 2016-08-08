import numpy as np
import cv2
from db import *




all_rows = Avtonomera.select()


scaled_img_path = '/home/naz/Desktop/avto_6500/all_img_scaled'




for row in all_rows:

    img = cv2.imread(scaled_img_path + '/' + row.name, 1)

    print row.name

    objects = json.loads(row.scaled_points)

    for object in objects:
        points_arr = []

        for point in object:
            points_arr.append([point['x'], point['y']])


        rect = cv2.boundingRect(np.array(points_arr))
        margin = rect[3]/3
        cv2.rectangle(img, (rect[0] - margin, rect[1] - margin), (rect[0] + rect[2] + margin, rect[1] + rect[3] + margin), (255,0,0), 2)


        pts = np.array(points_arr, np.int32)
        pts = pts.reshape((-1,1,2))

        cv2.polylines(img,[pts],True,(0,0,255), 2)


        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




