import numpy as np
import cv2
from db import *




all_rows = Avtonomera.select()


scaled_img_path = '/home/naz/Desktop/avto_6500/all_img_scaled'




for row in all_rows:

    img = cv2.imread(scaled_img_path + '/' + row.name, 1)

    bounding_rects = json.loads(row.bounding_rects)

    for bounding_rect in bounding_rects:

        cv2.rectangle(img, (bounding_rect[0], bounding_rect[1]), (bounding_rect[2], bounding_rect[3]), (255,0,0), 2)

        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




