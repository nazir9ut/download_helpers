import numpy as np
import cv2
from db import *




all_rows = Avtonomera.select()


scaled_img_path = '/home/naz/Desktop/avto_6500/all_img_scaled'




for row in all_rows:

    img = cv2.imread(scaled_img_path + '/' + row.name, 1)

    print row.name

    objects = json.loads(row.scaled_points)

    points_arr = []

    for object in objects:
        for point in object:
            points_arr.append([point['x'], point['y']])


    pts = np.array(points_arr, np.int32)
    pts = pts.reshape((-1,1,2))

    cv2.polylines(img,[pts],True,(0,0,255), 2)


    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




